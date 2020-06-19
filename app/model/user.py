from werkzeug.security import generate_password_hash, check_password_hash
from app.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, **kwargs) -> None:
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(self.password)

    def __repr__(self) -> str:
        return '<User %s>' % self.email

    def serialize(self) -> dict:
        data = {
            'id': str(self.id),
            'email': self.email
        }

        return data


class UserUtil:

    def get_by_email(self, email: str) -> User:
        return User.query.filter(User.email == email).first()

    def is_invalid(self, data: {}, check_user=True) -> list:
        invalid = list()

        email = data.get('email')
        password = data.get('password')

        if check_user:
            user_checking = self.get_by_email(email)
            if user_checking:
                invalid.append({"email": "is already in use."})

            if not email:
                invalid.append({"email": "must be filled"})

        if not password:
            invalid.append({"password": "must be filled"})

        if password and len(password) < 8:
            invalid.append({"password": "minimum length of 8 characters"})

        return invalid

    def authenticate(self, email: str, password: str) -> bool:
        user = self.get_by_email(email)
        if user and check_password_hash(user.password, password):
            return user

        return False

    def update(self, user: User, password: str) -> None:
        user.password = generate_password_hash(password)
        db.session.commit()

    def delete(self, user: User) -> int:
        deleted = db.session.delete(user)
        db.session.commit()

        return deleted
