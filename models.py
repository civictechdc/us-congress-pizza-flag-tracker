# ORM models for State, Order, User and Log db
from sqlalchemy import func
from config import db

# id, State, Order Number, COffice, created_at , updated_at

class OfficeModel(db.Model):
    __tablename__ = "offices"
    usa_state = db.Column(db.String(10))
    office_code = db.Column(db.String(10), primary_key=True, nullable=False) 
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    orders = db.relationship("OrderModel")
    statuses = db.relationship("StatusModel")
     
    def __init__(self, usa_state, office_code, office_name):
        self.office_code = office_code
        self.usa_state = usa_state
        self.created_at = func.now()
        self.updated_at = server_default = func.now()
        
class OrderModel(db.Model):
    __tablename__ = "orders"
    order_number = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(10))
    office_code = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    #home_office_code = db.relationship("offices", foreign_keys=["office_code"])
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, theUuid, usa_state, order_number, office_code):
        self.uuid = theUuid
        self.usa_state = usa_state
        self.order_number = order_number
        self.office_code = office_code
        created_at = db.Column(db.DateTime, server_default=func.now())
        updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

# Terence: When we create the new table for statuses
#  we'll need foreign keys in our ORM
#  for statuses. Every order has a status but
#  statuses have many orders.

#Do we want to break this file up into separate model
#  files? E.g. statusModels.py, userModels.py

# id (number), office code (string), sequence_num (numerical), description (text)
#Status notes (Where orders are from)
#  id (number),
#  office code (string),
#  sequence_num (numerical),
#  description (text)
class StatusModel(db.Model):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    office_code = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    sequence_num = db.Column(db.Integer)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
    def __init__(self, id, office_code, sequence_num, description):
        self.id = id
        self.office_code = office_code
        self.sequence_num = sequence_num
        self.description = description
        created_at = db.Column(db.DateTime, server_default=func.now())
        updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


#User Table notes
#  uuid, user_id, can_set_status (if they scan), (one to many)
class UserParams:
    username: str
    password: str
    can_create_update_delete_orders: str
    can_update_password_for: str
    can_update_status_for: str
    is_admin: str


class UserModel(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(10), primary_key=True)
    password = db.Column(db.String(100))
    can_update_status_for = db.Column(db.String(10))
    can_update_password_for = db.Column(db.String(10))
    can_create_update_delete_orders = db.Column(db.String(1))
    is_admin = db.Column(db.String(1))



    def __init__(self, user_values: UserParams):
        self.username = user_values.username
        self.password = user_values.password
        self.can_create_update_delete_orders = user_values.can_create_update_delete_orders
        self.can_update_status_for = user_values.can_update_status_for
        self.can_update_password_for = user_values.can_update_password_for
        self.is_admin = user_values.is_admin


