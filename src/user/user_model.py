# ORM models for State, Order, User and Log db
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join
from config import db


# id, State, Order Number, COffice, created_at , updated_at
from src.office.office_model import OfficeModel

# User Table notes
#  uuid, user_id, can_set_status (if they scan), (one to many)
class UserParams:
    username: str
    password: str
    office_code: str
    manage_all_orders: str
    update_all_statuses: str
    view_all_orders: str
    manage_all_users: str
    manage_office_users: str
    update_own_password: str
    can_create_update_delete_orders: str
    can_update_password_for: str
    can_update_status_for: str
    is_admin: str

class UserModel(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.LargeBinary(length=2048))
    office_code = db.Column(
        db.String(10), db.ForeignKey(OfficeModel.office_code))
    manage_all_orders = db.Column(db.String(1))
    update_all_statuses = db.Column(db.String(1))
    view_all_orders = db.Column(db.String(1))
    manage_all_users = db.Column(db.String(1))
    manage_office_users = db.Column(db.String(1))
    update_own_password = db.Column(db.String(1))
    can_update_status_for = db.Column(db.String(20))
    can_update_password_for = db.Column(db.String(20))
    can_create_update_delete_orders = db.Column(db.String(1))
    is_admin = db.Column(db.String(1))

    def __init__(self, user_values: UserParams):
        self.username = user_values.username
        self.password = user_values.password
        self.office_code = user_values.office_code
        self.manage_all_orders = user_values.manage_all_orders
        self.update_all_statuses = user_values.update_all_statuses
        self.view_all_orders = user_values.view_all_orders
        self.manage_all_users = user_values.manage_all_users
        self.manage_office_users = user_values.manage_office_users
        self.update_own_password = user_values.update_own_password
        self.can_create_update_delete_orders = user_values.can_create_update_delete_orders
        self.can_update_status_for = user_values.can_update_status_for
        self.can_update_password_for = user_values.can_update_password_for
        self.is_admin = user_values.is_admin
