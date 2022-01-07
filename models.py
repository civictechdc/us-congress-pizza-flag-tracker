# ORM models for State, Order, User and Log db
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join
from config import db


# id, State, Order Number, COffice, created_at , updated_at

class OfficeModel(db.Model):
    __tablename__ = "offices"
    # TODO(tdk): commenting out uuid as this may not be needed with un/pw login
    # uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    office_code = db.Column(db.String(10), primary_key=True, nullable=False)
    usa_state = db.Column(db.String(10))
    users = db.relationship("UserModel")
    orders = db.relationship("OrderModel")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, usa_state, office_code):
        # see above about not needing uuid
        # self.uuid = theUuid
        self.office_code = office_code
        self.usa_state = usa_state


# Do we want to break this file up into separate model
#  files? E.g. statusModels.py, userModels.py

class StatusModel(db.Model):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    sequence_num = db.Column(db.Integer)
    description = db.Column(db.String(255))
    permission = db.Column(db.String(255))
    active_status = db.Column(db.String(255))
    status_code = db.Column(db.String(255))
    orders = db.relationship('OrderModel', back_populates="status")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, id, sequence_num, description, permission, active_status, status_code):
        self.id = id
        self.sequence_num = sequence_num
        self.description = description
        self.permission = permission
        self.active_status = active_status
        self.status_code = status_code


# User Table notes
#  uuid, user_id, can_set_status (if they scan), (one to many)
class UserParams:
    username: str
    password: str
    office_code: str
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
    can_update_status_for = db.Column(db.String(20))
    can_update_password_for = db.Column(db.String(20))
    can_create_update_delete_orders = db.Column(db.String(1))
    is_admin = db.Column(db.String(1))

    def __init__(self, user_values: UserParams):
        self.username = user_values.username
        self.password = user_values.password
        self.office_code = user_values.office_code
        self.can_create_update_delete_orders = user_values.can_create_update_delete_orders
        self.can_update_status_for = user_values.can_update_status_for
        self.can_update_password_for = user_values.can_update_password_for
        self.is_admin = user_values.is_admin
