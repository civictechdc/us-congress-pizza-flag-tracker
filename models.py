# ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from config import db

# id, State, Order Number, COffice, created_at , updated_at

class OrderModel(db.Model):
    __tablename__ = "orders"
    order_number = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(255))
    coffice = db.Column(db.String(255))
    #home_office_code = db.relationship("agency_offices", foreign_keys=["agency_office_code"])
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, theUuid, usa_state, order_number, coffice):
       self.usa_state = usa_state
       self.order_number = order_number
       self.coffice = coffice
       self.uuid = theUuid


class AgencyOfficeModel(db.Model):
    __tablename__ = "agency_offices"
    agency_office_code = db.Column(db.String(50), primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(20))
    agency_office_name = db.Column(db.String(255))
    can_set_status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
     
    def __init__(self, agency_office_code, uuid, usa_state, agency_office_name, can_set_status):
        self.agency_office_code = agency_office_code
        self.uuid = uuid
        self.usa_state = usa_state
        self.agency_office_name = agency_office_name
        self.can_set_status = can_set_status




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
