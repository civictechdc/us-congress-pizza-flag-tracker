from hashlib import new
import os

import bcrypt
from werkzeug.exceptions import Unauthorized
from src.auth import auth_privileges
from src.auth.auth_actions import AuthActions
from src.user.user_model import UserModel, UserParams
from src.order.order_model import OrderModel
from src.auth.auth_controller import get_current_user
from flask_sqlalchemy import sqlalchemy
from config import db, flask_app
import uuid

from src.util import table_record_to_json, table_to_json

import datetime

import jwt
from flask import request, make_response, jsonify

from flask_sqlalchemy import sqlalchemy
from config import db, flask_app
import uuid

from src.util import table_record_to_json, table_to_json


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
        #only admin can see users
        #need a verify user function to check for admin previlages

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
        db.session.commit()
        return user

    @classmethod
    def update_password(cls, user, new_password):
        user.password = new_password
        bcrypt_rounds = int (os.environ["BCRYPT_ROUNDS"])
        salt = bcrypt.gensalt(bcrypt_rounds)
        new_hashed_password = bcrypt.hashpw(user.password.encode(), salt)
        user.password = new_hashed_password
        db.session.commit()
        return user

    @classmethod
    def self_update_password(cls, username, new_password, old_password):
        user = AuthActions.fetch_user(username, old_password)
        cls.update_password(user, new_password)
        return username

    @classmethod
    def admin_update_password(cls, username, new_password):
        has_permission = False
        current_user = get_current_user()
        user = cls.get_by_name(username)
        if current_user.username == "FED-ADMIN":
            has_permission = True
        elif current_user.is_admin and current_user.office_code == user.office_code:
            has_permission = True
        if has_permission:
            cls.update_password(user, new_password)
            return
        else:
            raise Unauthorized("Unauthorized. Admin privileges required.")

            