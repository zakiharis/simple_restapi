from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = None
migrate = None


def init(app: Flask) -> None:
    global db, migrate

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
