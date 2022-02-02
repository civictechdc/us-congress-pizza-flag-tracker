from config import db
from src.log.log_actions import LogModel
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join

class LogModel(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    order_number = db.Column(db.Interger)
    home_office_code=db.Column(db.String(10))
    status_code = db.Column(db.String(255))
    #order_status_id
    active_status = db.Column(db.String(255))
    #previouse_status_code
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
        #order_status_id
        self.active_status = active_status
        #previouse_status_code
        self.status_description = status_description
        self.order_updated_at = order_updated_at
