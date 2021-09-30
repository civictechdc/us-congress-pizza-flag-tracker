# ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from sqlalchemy.orm import relationship
from config import db

# id, State, Order Number, COffice, created_at , updated_at

class OfficeModel(db.Model):
    __tablename__ = "offices"
    # TODO(tdk): commenting out uuid as this may not be needed with un/pw login
    # uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    office_code = db.Column(db.String(10), primary_key=True, nullable=False) 
    orders = db.relationship("OrderModel")
    statuses = db.relationship("StatusModel")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    usa_state = db.Column(db.String(10))


    def __init__(self, usa_state, office_code):
        
        #see above about not needing uuid
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

    home_office_code = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    # Ordermodel needs status relationship
    # Need status relationship

    def __init__(self, theUuid, usa_state, order_number, home_office_code):
        self.uuid = theUuid
        self.usa_state = usa_state
        self.order_number = order_number
        self.home_office_code = home_office_code
        # self.updated_by = "HOSS"

#Do we want to break this file up into separate model
#  files? E.g. statusModels.py, userModels.py

class StatusModel(db.Model):
    __tablename__ = "status"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    status_federal_office_code = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    sequence_num = db.Column(db.Integer)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    
    def __init__(self, id, status_federal_office_code, sequence_num, description):
        self.id = id
        self.status_federal_office_code = status_federal_office_code
        self.sequence_num = sequence_num
        self.description = description


#User Table notes
#  uuid, user_id, can_set_status (if they scan), (one to many)

