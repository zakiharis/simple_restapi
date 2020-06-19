from fabric.tasks import task


@task
def provision(c):
    # update apt
    cmd = "apt update"
    sudo_cmd(c, cmd)

    # install apt packages
    cmd = "apt -y install python-pip python-dev nginx git"
    sudo_cmd(c, cmd)

    # get latest source code from github
    cmd = "git clone https://github.com/zakiharis/simple_restapi"
    run_cmd(c, cmd)

    # install library from pip
    cmd = "pip install -r simple_restapi/requirements.txt"
    run_cmd(c, cmd)

    # copy systemd service file
    cmd = "cp simple_restapi/deployment/simple_restapi.service /etc/systemd/system/"
    sudo_cmd(c, cmd)

    # enable simple_restapi service
    cmd = "systemctl enable simple_restapi"
    sudo_cmd(c, cmd)

    # start simple_restapi service
    cmd = "systemctl start simple_restapi"
    sudo_cmd(c, cmd)

    # remove nginx default config
    cmd = "rm /etc/nginx/sites-enabled/default"
    sudo_cmd(c, cmd)

    # copy simple_restapi nginx config
    cmd = "cp simple_restapi/deployment/mysimplerestapitest.ml.conf /etc/nginx/sites-available/"
    sudo_cmd(c, cmd)

    # enable simple_restapi nginx config
    cmd = "ln -s /etc/nginx/sites-available/mysimplerestapitest.ml.conf /etc/nginx/sites-enabled/"
    sudo_cmd(c, cmd)

    # restart nginx
    cmd = "systemctl restart nginx"
    sudo_cmd(c, cmd)


@task
def update(c):
    cmd = "cd simple_restapi; git pull"
    run_cmd(c, cmd)


def sudo_cmd(c, cmd):
    result = c.sudo(cmd)
    print(result)


def run_cmd(c, cmd):
    result = c.run(cmd)
    print(result)
