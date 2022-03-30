# import re
from src.order_log.order_log_model import OrderLogModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from src.order.order_actions import OrderActions
from config import db
import uuid

class LogActions:
    @classmethod
    def create_order_log(cls, usa_state, order_number, home_office_code, order_status_id):
        get_order_uuid = OrderActions.get_order_by_order_number(order_number)
        order_uuid = get_order_uuid.uuid
        get_previous_order_log_uuid = LogActions.get_order_log_uuid(order_number)
        previous_order_log_uuid = get_previous_order_log_uuid
        logUuid = str(uuid.uuid4())
        new_log = OrderLogModel(logUuid = logUuid, order_number = order_number, previous_order_log_uuid = previous_order_log_uuid, order_uuid = order_uuid, usa_state = usa_state, home_office_code =home_office_code, order_status_id= order_status_id)
        db.session.add(new_log)
        db.session.commit()
        return new_log

    @classmethod
    def get_order_log_uuid(cls, order_num):
        order_nums = OrderLogModel.query.filter(OrderLogModel.order_number == order_num).all()
        get_order_uuid = None
        for order in order_nums:
            get_order_uuid = order.uuid
        
        if get_order_uuid == None: 
            return get_order_uuid
        else:
            return get_order_uuid
        
    @classmethod
    def get_all_order_logs(cls):
        get_order_logs = OrderLogModel.query.all()
        return get_order_logs
    
    @classmethod
    def get_all_order_logs_by_order_number(cls, order_number):
        get_all_logs_by_order_number = OrderLogModel.query.get(order_number).all()
        return get_all_logs_by_order_number
        