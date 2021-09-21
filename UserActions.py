from models import UserModel, OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid


class UserActions:
    # Table actions:

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
        return [{"name": user.name, "email": user.email} for user in users]

    @classmethod
    def get_by_code(cls, email: str):
        return UserModel.query.filter(UserModel.email == email).first()

    @classmethod
    def update_user(cls, uuid, name, user_number, email):
        user = cls.get_user_by_uuid(uuid)
        user.user_number = user_number
        user.name = name
        user.email = email
        db.session.commit()
        return user
