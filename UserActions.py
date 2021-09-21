<<<<<<< HEAD


from models import UserModel, OrderModel, UserParams
from flask_sqlalchemy import sqlalchemy
from config import db, app
import uuid

from util import table_record_to_json, table_to_json

=======
from models import UserModel, OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid

>>>>>>> 34b152c (Signup manually tested through postman and corrected)

class UserActions:
    # Table actions:

    @classmethod
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

    @classmethod
    def get_by_code(cls, email: str):
        return UserModel.query.filter(UserModel.email == email).first()

    @classmethod
    def update_user(cls, uuid, name, user_number, email):
        user = cls.get_user_by_uuid(uuid)
        user.user_number = user_number
        user.name = name
        user.email = email
>>>>>>> 34b152c (Signup manually tested through postman and corrected)
        db.session.commit()
        return user
