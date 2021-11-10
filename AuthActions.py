import datetime

import bcrypt
import jwt
from werkzeug.exceptions import Unauthorized

from util import get_http_response
from config import flask_app

from models import UserModel, UserParams
from util import table_record_to_json


class AuthActions:
    @classmethod
    def fetch_user(cls, username: str, password: str):
        user = UserModel.query.filter_by(username=username).first()
        if not user:
            raise Unauthorized("Invalid username.")

        if not bcrypt.checkpw(password.encode(), user.password):
            raise Unauthorized("Invalid password.")

        return table_record_to_json(user)
