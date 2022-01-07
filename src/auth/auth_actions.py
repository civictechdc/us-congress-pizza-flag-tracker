import datetime

import bcrypt
import jwt
from werkzeug.exceptions import Unauthorized
from src.user.user_model import UserModel

class AuthActions:
    @classmethod
    def fetch_user(cls, username: str, password: str):
        user = UserModel.query.filter_by(username=username).first()
        if not user:
            raise Unauthorized("Invalid username.")

        if not bcrypt.checkpw(password.encode(), user.password):
            raise Unauthorized("Invalid password.")

        return user
