from config import db
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join
from src.order.order_model import OrderModel
from src.office.office_model import OfficeModel

class LogModel(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    order_number = db.Column(db.Interger)
    home_office_code=db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    status_code = db.Column(db.String(255)) #foreign key
    order_status_id = db.Column(db.String(255), db.ForiegnKey('status.id'))
    active_status = db.Column(db.String(255)) #foreign key
    #previouse_status_code #foreign key
    status_description = db.Column(db.String(255)) #foreign key
    order_updated_at = db.Column(db.DateTime) 
    status= db.relationship('Status Model', back_populates='orders') #check this back_population
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, id, order_number, home_office_code, status_code, order_status_id, active_status, status_description, order_updated_at):
        self.id = id
        self.order_number = order_number
        self.home_office_code = home_office_code
        self.status_code = status_code
        order_status_id = order_status_id
        self.active_status = active_status
        #previouse_status_code
        self.status_description = status_description
        self.order_updated_at = order_updated_at
