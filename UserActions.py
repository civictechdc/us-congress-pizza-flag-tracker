import datetime

import jwt
from flask import request, make_response, jsonify

from models import UserModel, OrderModel, UserParams
from flask_sqlalchemy import sqlalchemy
from config import db, app
import uuid

from util import table_record_to_json, table_to_json


class UserActions:
    # Table actions:

    @classmethod
    def login_user(cls):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response(
                "could not verify", 401, {"Authentication": 'login required"'}
            )
        user = UserModel.query.filter_by(username=auth.username).first()
        # if check_password_hash(user.password, auth.password):
        if user.password == auth.password:
            token = jwt.encode(
                {
                    "public_id": user.username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=45),
                },
                app.config["SECRET_KEY"],
                "HS256",
            )
            return jsonify({"accessToken": token})

        return make_response(
            "could not verify", 401, {"Authentication": '"login required"'}
        )

    @classmethod
    def create(
        cls,
        user_values: UserParams
    ):
        new_user = UserModel(user_values)
        db.session.add(new_user)
        db.session.commit()
        return table_record_to_json(new_user)

    @classmethod
    def get_users(cls):
        users = UserModel.query.all()
        return users

    @classmethod
    def get_by_name(cls, username: str):
        return UserModel.query.filter(UserModel.username == username).first()

    @classmethod
    def update_user(cls, user_values: UserParams):
        user = cls.get_by_name(user_values.username)
        user.password = user_values.password
        user.can_create_update_delete_orders = user_values.can_create_update_delete_orders
        user.can_update_password_for=user_values.can_update_password_for
        user.can_update_status_for=user_values.can_update_status_for
        user.is_admin = user_values.is_admin
        db.session.commit()
        return user
