# Simple REST API

This repo contains answers to paynet software engineer quiz

# Live Demo

https://mysimplerestapitest.ml/

# Setting Up Development Env

  - Required Python3.6+
  - Clone this repo
  - Install the dependencies (recommended to use the venv to create a virtual environment)
    ```sh
    $ cd simple_restapi
    $ pip install -r requirements.txt
    ```
  - Rename `local.env` to `.env`
  - Perform database migration
    ```sh
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
    ```
  - Start the development server
    ```sh
    $ flask run
    ```
    
# Tests

Run the test with the following command:
```
pytest tests/
```

# APIs

| # | Route | Method | Payload | Full route | Description |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | /auth/register | POST | Body -> {"email": "abc@abc.com", "password": "abc12345"} | https://mysimplerestapitest.ml/auth/register | Create a new user |
| 2 | /auth/login | POST | Body -> {"email": "abc@abc.com", "password": "abc12345"} | https://mysimplerestapitest.ml/auth/login | Login a user and get a JWT token |
| 3 | /auth/logout | GET | Header -> Authorization: Bearer [JWT Token] | https://mysimplerestapitest.ml/auth/logout | Sign out and blacklist the JWT token |
| 4 | /auth/refresh | POST | Header -> Authorization: Bearer [JWT Refresh Token] | https://mysimplerestapitest.ml/auth/refresh | Get a new JWT token |
| 5 | /auth/key | GET | Header -> Authorization: Bearer [JWT Token] | https://mysimplerestapitest.ml/auth/key | Get a public key to encrypt a message |
| 6 | /auth/decode | POST | Header -> Authorization: Bearer [JWT Token] Body -> {"encrypted_message": "[base64 of the encrypted json]"} | https://mysimplerestapitest.ml/auth/decode | Validate that server is able to decrypt the encrypted message |
| 7 | /account | GET | Header -> Authorization: Bearer [JWT Token] | https://mysimplerestapitest.ml/account | Get the user account details |
| 8 | /account | PUT | Header -> Authorization: Bearer [JWT Token] Body -> {"password": "mYn3wp@ssw0rd"} | https://mysimplerestapitest.ml/account | Update the user password |
| 9 | /account | DELETE | Header -> Authorization: Bearer [JWT Token] | https://mysimplerestapitest.ml/account | Delete the user account |

# Testing AES256 encrypted value

Run `secret_message_generator.py` and follow the instructions. This small python script will encrypt the message using server public key and return as a base64. Use /auth/decode api to verify the message. ***/auth/decode*** will decode the base64, then decrypt the encrypted message using server private key
