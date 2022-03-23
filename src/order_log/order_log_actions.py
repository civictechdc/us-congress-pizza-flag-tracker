# import re
from src.order_log.order_log_model import OrderLogModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from config import db
import uuid

class LogActions:
    @classmethod
    def log(cls, previous_order_log_id, order_number, order_uuid, usa_state, home_office_code, order_status_id):
        logUuid = str(uuid.uuid4())
        new_log = OrderLogModel(logUuid, previous_order_log_id, order_number, order_uuid, usa_state, home_office_code, order_status_id)
        db.session.add(new_log)
        db.session.commit()
        return new_log

    @classmethod
    def get_order_log_id(cls, order_num):
        order_num = OrderLogModel.query.filter(OrderLogModel.order_number == order_num).first()
        if order_num.previous_order_log_id == None:
            previous_log_id = "NewOrder"
            return previous_log_id
        else:
            previous_log_id = order_num.previous_order_log_id 
            return previous_log_id
    
    @classmethod
    def get_all_logs(cls):
        get_logs = OrderLogModel.query.all()
        return get_logs
    
    @classmethod
    def get_all_order_logs_by_order_number(cls, order_number):
        get_all_logs_by_order_number = OrderLogModel.query.order_by(order_number).all()
        return get_all_logs_by_order_number
        