import re
from src.log.log_model import LogModel
from src.status.status_model import StatusModel
from config import db

class LogActions:
    @classmethod
    def log(cls, order):
        
        db.session.add(order)
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
    