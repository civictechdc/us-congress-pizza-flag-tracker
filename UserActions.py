import os

import bcrypt

from src.auth import auth_privileges
from models import UserModel, UserParams
from src.order.order_models import OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db, flask_app
import uuid

from util import table_record_to_json, table_to_json

import datetime

import jwt
from flask import request, make_response, jsonify

from flask_sqlalchemy import sqlalchemy
from config import db, flask_app
import uuid

from util import table_record_to_json, table_to_json


class UserActions:
    # Table actions:

    @classmethod
    def create(cls, user_values: UserParams):
        new_user = UserModel(user_values)
        bcrypt_rounds = int (os.environ["BCRYPT_ROUNDS"])
        salt = bcrypt.gensalt(bcrypt_rounds)
        hashed_password = bcrypt.hashpw(new_user.password.encode(), salt)
        new_user.password = hashed_password
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def delete(cls):
        UserModel.query.delete()
        db.session.commit()

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
        user.can_create_update_delete_orders = (
            user_values.can_create_update_delete_orders
        )
        user.can_update_password_for = user_values.can_update_password_for
        user.can_update_status_for = user_values.can_update_status_for
        auth_privileges.is_admin = user_values.is_admin
