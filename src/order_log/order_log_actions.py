# import re
from src.order_log.order_log_model import OrderLogModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from config import db
import uuid

class LogActions:
    @classmethod
    def create_order_log(cls, order_uuid, usa_state, order_number, home_office_code, order_status_id):
        prior_order_log_uuid = LogActions.get_order_log_uuid(order_number)
        previous_order_log_uuid = prior_order_log_uuid
        logUuid = str(uuid.uuid4())
        new_log = OrderLogModel(logUuid = logUuid, order_number = order_number, previous_order_log_uuid = previous_order_log_uuid, order_uuid = order_uuid, usa_state = usa_state, home_office_code =home_office_code, order_status_id= order_status_id)
        db.session.add(new_log)
        db.session.commit()
        return new_log

    @classmethod
    def get_order_log_uuid(cls, order_num):
        order_logs = OrderLogModel.query.filter(OrderLogModel.order_number == order_num).all()
        order_log_uuid = None
        #sort this object
        for order in order_logs:
            order_log_uuid = order.uuid
        return order_log_uuid      
        
    @classmethod
    def get_all_order_logs(cls):
        order_logs = OrderLogModel.query.all()
        return order_logs
    
    @classmethod
    def get_all_order_logs_by_order_number(cls, order_number):
        order_log_obj = OrderLogModel.query.get(order_number).all()
        return order_log_obj
        