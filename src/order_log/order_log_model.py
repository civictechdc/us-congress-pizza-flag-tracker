from tarfile import USTAR_FORMAT
from urllib.parse import uses_params
from config import db
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join
from src.order.order_model import OrderModel
from src.office.office_model import OfficeModel

class OrderLogModel(db.Model):
    __tablename__ = "order_logs"
    uuid = db.Column(db.String(40), unique=True, index=True, primary_key=True, nullable=False)
    order_number = db.Column(db.Integer)
    previous_order_log_uuid = db.Column(db.String(255), nullable = True)
    order_updated_at = db.Column(db.DateTime, server_default=func.now())
    order_uuid = db.Column(db.String(40), db.ForeignKey(OrderModel.uuid))
    usa_state = db.Column(db.String(10))
    home_office_code=db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    order_status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    status = db.relationship('StatusModel', back_populates='order_logs')
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, logUuid, order_number, previous_order_log_uuid, order_uuid, usa_state, home_office_code, order_status_id):
        self.uuid = logUuid
        self.order_number = order_number
        self.previous_order_log_uuid = previous_order_log_uuid
        self.order_uuid = order_uuid
        self.usa_state = usa_state 
        self.home_office_code = home_office_code
        self.order_status_id = order_status_id
