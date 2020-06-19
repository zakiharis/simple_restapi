import pytest

from app import create_app


def init_db() -> None:
    from app.database import db
    db.create_all()


def drop_db() -> None:
    from app.database import db
    db.drop_all()


def create_test_user() -> None:
    from app.model import User
    from werkzeug.security import generate_password_hash
    from app.database import db

    user = User.query.filter(User.email == 'test@test.com').first()

    if not user:
        user = User(email='test@test.com', password=generate_password_hash('test1234'))
        db.session.add(user)
        db.session.commit()


@pytest.fixture
def app(request):
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/test_app.db',
        'JWT_BLACKLIST_ENABLED': True,
        'JWT_BLACKLIST_TOKEN_CHECKS': ['access', 'refresh'],
        'SECRET_KEY': 'dev',
        'JWT_SECRET_KEY': 'dev'
    })

    ctx = app.app_context()
    ctx.push()

    def teardown():
        drop_db()
        init_db()
        ctx.pop()

    init_db()
    create_test_user()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def client(app):
    return app.test_client()


@pytest.fixture
def auth(app, request):
    from flask_jwt_extended import (create_access_token, create_refresh_token)

    access_token_encoded = create_access_token(identity='test@test.com')
    refresh_token_encoded = create_refresh_token(identity='test@test.com')

    headers = {
        'access_token': {'Authorization': 'Bearer ' + access_token_encoded},
        'refresh_token': {'Authorization': 'Bearer ' + refresh_token_encoded},
    }

    return headers
