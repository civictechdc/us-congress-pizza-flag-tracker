from config import db

from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join

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