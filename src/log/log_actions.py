import re
from src.log.log_model import LogModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from config import db

class LogActions:
    @classmethod
    def log(cls, usa_state, idbased_order_number, home_office_code, order_status_id):
        order_number = idbased_order_number
        current_status = StatusModel.query.filter_by(order_status_id).first() 
        active_status = current_status.active_status
        status_description = current_status.status_description
        previous_status_code = active_status
        new_log= LogModel(usa_state, order_number, home_office_code, order_status_id, active_status, status_description, previous_status_code)
        db.session.add(new_log)
        db.session.commit()
        return

    @classmethod
    def update(cls, order):
        
        db.session.commit()
        return

    @classmethod
    def get_all_logs(cls):
        get_logs = LogModel.query.all()
        return get_logs
    