import os

from flask import Flask
from flask_jwt_extended import JWTManager


def create_app(test_config: dict = {}) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.jwt_blacklist = set()
    app.jwt_tokenlist = {}

    load_config(app, test_config)

    init_database(app)
    init_blueprints(app)
    init_jwt_manager(app)

    return app


def load_config(app: Flask, test_config) -> None:
    if os.environ.get('FLASK_ENV') == 'development' or test_config.get("FLASK_ENV") == 'development':
        app.config.from_object('app.config.Development')

    elif test_config.get('TESTING'):
        app.config.from_mapping(test_config)

    else:
        app.config.from_object('app.config.Production')


def init_database(app: Flask) -> None:
    from .database import init
    init(app)


def init_blueprints(app: Flask) -> None:
    from .blueprint.handlers import register_handler
    register_handler(app)

    from .blueprint import index, auth, account
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(account.bp)


def init_jwt_manager(app: Flask) -> None:
    jwt = JWTManager(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in app.jwt_blacklist
