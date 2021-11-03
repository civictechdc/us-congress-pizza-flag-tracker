import datetime

import jwt
from flask import request, make_response

from UserActions import UserActions
from config import flask_app
from models import UserModel, UserParams
from util import table_record_to_json


class AuthActions:
    @classmethod
    def create_admin_user(cls, username: str, password: str):
        params = UserParams()
        params.username = username
        params.password = password
        params.can_update_status_for = "ALL"
        params.can_update_password_for = "ALL"
        params.can_create_update_delete_orders = "Y"
        params.is_admin = "Y"
        UserActions.create(params)

    @classmethod
    def login_user(cls, username, password):
        print("user debug", username, password)
        user = UserModel.query.filter_by(username=username).first()
         # if check_password_hash(user.password, auth.password):
        if user.password == password:
            ret_val = table_record_to_json(user)
            ret_val["accessToken"] = AuthActions.get_token(user.username)
            return ret_val

        return make_response(
            "could not verify", 401, {"Authentication": "login required"}
        )

    @classmethod
    def get_token(cls, username):
        token = jwt.encode(
            {
                "public_id": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=45),
            },
            flask_app.config["SECRET_KEY"],
            "HS256",
        )
        return token
