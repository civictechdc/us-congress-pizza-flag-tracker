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


class OrderModel(db.Model):
    __tablename__ = "orders"
    order_number = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(10))
    # updated_by = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    # error when you uncomment ^
    # sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class OfficeModel->offices'. Original exception was: Could not determine join condition between parent/child tables on relationship OfficeModel.orders - there are multiple foreign key paths linking the tables.  Specify the 'foreign_keys' argument, providing a list of those columns which should be counted as containing a foreign key reference to the parent table.
    order_status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    home_office_code = db.Column(
        db.String(10), db.ForeignKey(OfficeModel.office_code))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())
    status=db.relationship("StatusModel", back_populates="orders")

    # Ordermodel needs status relationship
    # Need status relationship
    # order_status_id = db.relationship('StatusModel',backref = 'orders', lazy = True)

    def __init__(self, theUuid, usa_state, order_number, home_office_code, order_status_id, order_status=None):
        self.uuid = theUuid
        self.usa_state = usa_state
        self.order_number = order_number
        self.home_office_code = home_office_code
        if order_status_id:
            self.order_status_id = order_status_id
        elif order_status:
            self.order_status_id = order_status.id
        # self.updated_by = "HOSS"uus

    def update_order(self, usa_state=None, order_number=None, home_office_code=None, order_status_id=None, order_status=None):
        self.order_number = order_number or self.order_number
        self.usa_state = usa_state or self.usa_state
        self.home_office_code = home_office_code or self.home_office_code
        if order_status_id:
            self.order_status_id = order_status_id
        else:
            self.order_status = order_status


# Do we want to break this file up into separate model
#  files? E.g. statusModels.py, userModels.py

class StatusModel(db.Model):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    sequence_num = db.Column(db.Integer)
    description = db.Column(db.String(255))
    active_status = db.Column(db.String(255))
    status_code = db.Column(db.String(255))
    orders = db.relationship('OrderModel', back_populates="status")
    # order_no = db.Column(db.Integer, db.ForeignKey('orders.order_number'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, id, sequence_num, description, active_status, status_code):
        self.id = id
        self.sequence_num = sequence_num
        self.description = description
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

#Log Table
#id, order_number, home_office_code, status_code, active_status, status_description, order_updated_at

class LogModel(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    order_number = db.Column(db.Interger)
    home_office_code=db.Column(db.String(10))
    status_code = db.Column(db.String(255))
    active_status = db.Column(db.String(255))
    status_description = db.Column(db.String(255))
    order_updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, id, order_number, home_office_code, status_code, active_status, status_description, order_updated_at):
        self.id = id
        self.order_number = order_number
        self.home_office_code = home_office_code
        self.status_code = status_code
        self.active_status = active_status
        self.status_description = status_description
        self.order_updated_at = order_updated_at
