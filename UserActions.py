import datetime

import jwt
from flask import request, make_response, jsonify

from models import UserModel, OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db, app
import uuid


class UserActions:
    # Table actions:

    @classmethod
    def login_user(cls):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'Authentication': 'login required"'})

        user = UserModel.query.filter_by(name=auth.username).first()
        # if check_password_hash(user.password, auth.password):
        if user.password == auth.password:
            token = jwt.encode(
                {'public_id': user.name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
                app.config['SECRET_KEY'], "HS256")
            return jsonify({'token': token})

        return make_response('could not verify', 401, {'Authentication': '"login required"'})

    @classmethod
    def create(cls, name: str, password: str):
        new_user = UserModel(name=name, password=password)
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
        return [{"name": user.name, "password": user.password} for user in users]

    @classmethod
    def get_by_name(cls, name: str):
        return UserModel.query.filter(UserModel.name == name).first()

    @classmethod
    def update_user(cls, name, password):
        user = cls.get_by_name(name)
        user.password = password
        db.session.commit()
        return user
