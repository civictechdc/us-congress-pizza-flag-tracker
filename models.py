# ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from sqlalchemy.orm import relationship
from config import db

# id, State, Order Number, COffice, created_at , updated_at

class OfficeModel(db.Model):
    __tablename__ = "offices"
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    office_code = db.Column(db.String(10), primary_key=True, nullable=False) 
    usa_state = db.Column(db.String(10))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    #orders = db.relationship("OrderModel")
    #statuses = db.relationship("StatusModel")
     
    def __init__(self, theUuid, office_code, usa_state):
        self.uuid = theUuid
        self.office_code = office_code
        self.usa_state = usa_state
        self.created_at = func.now()
        self.updated_at = server_default = func.now()
        
class OrderModel(db.Model):
    __tablename__ = "orders"
    order_number = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(10))
    updated_by = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    home_office_code = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # Ordermodel needs status relationship
    # Need status relationship

    def __init__(self, theUuid, usa_state, order_number):
        self.uuid = theUuid
        self.usa_state = usa_state
        self.order_number = order_number
        self.home_office_code = home_office_code
        self.updated_by = updated_by
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

