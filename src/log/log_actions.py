import re
from src.log.log_model import LogModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from config import db

class LogActions:
    @classmethod
    def log(cls, usa_state, idbased_order_number, home_office_code, order_status_id):
        current_status = Status.query.filter_by(order_status_id).first()    
        new_log= LogModel(usa_state, idbased_order_number, home_office_code, order_status_id, current_status)
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
    