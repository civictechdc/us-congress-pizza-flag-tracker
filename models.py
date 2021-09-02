# ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from sqlalchemy.orm import relationship
from config import db

# id, State, Order Number, COffice, created_at , updated_at

class OfficeModel(db.Model):
    __tablename__ = "offices"
    usa_state = db.Column(db.String(10))
    office_code = db.Column(db.String(10), primary_key=True, nullable=False)
    office_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    orders = db.relationship("OrderModel")
     
    def __init__(self, usa_state, office_code, office_name):
        self.office_code = office_code
        self.usa_state = usa_state
        self.office_name = office_name
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

#User Table notes
#  uuid, user_id, can_set_status (if they scan), (one to many)
