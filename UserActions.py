import datetime

import jwt
from flask import request, make_response, jsonify

from models import UserModel, OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db, app
import uuid

from util import table_record_to_json


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
        username: str,
        password: str,
        is_admin = "N",
        can_create_update_delete_orders = "NONE",
        can_update_password_for = "SELF",
        can_update_status_for = "SELF",
    ):
        new_user = UserModel(
            username=username,
            password=password,
            is_admin = is_admin,
            can_create_update_delete_orders = can_create_update_delete_orders,
            can_update_password_for = can_update_password_for,
            can_update_status_for = can_update_status_for
        )
        db.session.add(new_user)
        db.session.commit()
        return table_record_to_json(new_user)

    @classmethod
    def delete(cls):
        UserModel.query.delete()
        db.session.commit()

    @classmethod
    def get_users(cls):
        users = UserModel.query.all()
        return [{"username": user.username, "password": user.password} for user in users]

    @classmethod
    def get_by_name(cls, username: str):
        return UserModel.query.filter(UserModel.username == username).first()

    @classmethod
    def update_user(cls, username, password):
        user = cls.get_by_name(username)
        user.password = password
        db.session.commit()
        return user
