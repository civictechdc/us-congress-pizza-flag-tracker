import re
from src.order_log.order_log_model import LogModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from config import db

class LogActions:
    @classmethod
    def log(cls, usa_state, idbased_order_number, home_office_code, order_status_id):
        #get order number id based on the order number
        get_order_log_id = LogModel.query.order_by(order_number.previous_order_log_id.desc()).first() #this should query the last update
        home_office_code = usa_state
        order_number = idbased_order_number
        previous_order_log_id = get_order_log_id
        new_log= LogModel(order_number, home_office_code, previous_order_log_id, home_office_code, order_status_id)
        db.session.add(new_log)
        db.session.commit()
        return

    @classmethod
    def get_all_logs(cls):
        get_logs = LogModel.query.all()
        return get_logs
    
    @classmethod
    def get_all_order_logs_by_order_number(cls, order_number):
        get_all_logs_by_order_number = LogModel.query.order_by(order_number).all()
        return get_all_logs_by_order_number