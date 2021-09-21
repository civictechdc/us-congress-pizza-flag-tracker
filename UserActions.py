<<<<<<< HEAD
<<<<<<< HEAD


from models import UserModel, OrderModel, UserParams
from flask_sqlalchemy import sqlalchemy
from config import db, app
import uuid

from util import table_record_to_json, table_to_json

=======
=======
import datetime

import jwt
from flask import request, make_response, jsonify

>>>>>>> 6c52a99 (debugged sign in)
from models import UserModel, OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db, app
import uuid

>>>>>>> 34b152c (Signup manually tested through postman and corrected)

class UserActions:
    # Table actions:

    @classmethod
<<<<<<< HEAD
<<<<<<< HEAD
    def create(
        cls,
        user_values: UserParams
    ):
        new_user = UserModel(user_values)
        db.session.add(new_user)
        db.session.commit()
        return table_record_to_json(new_user)
=======
=======
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
>>>>>>> 6c52a99 (debugged sign in)
    def create(cls, name: str, password: str):
        new_user = UserModel(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def delete(cls):
        UserModel.query.delete()
        db.session.commit()
>>>>>>> 34b152c (Signup manually tested through postman and corrected)

    @classmethod
    def get_users(cls):
        users = UserModel.query.all()
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        return [{"name": user.name, "email": user.email} for user in users]
=======
        return [{"name": user.name, "password": user.password} for user in users]
>>>>>>> 6c52a99 (debugged sign in)

    @classmethod
    def get_by_name(cls, name: str):
        return UserModel.query.filter(UserModel.name == name).first()

    @classmethod
<<<<<<< HEAD
    def update_user(cls, uuid, name, user_number, email):
        user = cls.get_user_by_uuid(uuid)
        user.user_number = user_number
        user.name = name
        user.email = email
>>>>>>> 34b152c (Signup manually tested through postman and corrected)
=======
    def update_user(cls, name, password):
        user = cls.get_by_name(name)
        user.password = password
>>>>>>> 6c52a99 (debugged sign in)
        db.session.commit()
        return user
