from src.office.office_model import OfficeModel
from src.status.status_model import StatusModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid


class StatusActions:
    # Table actions:

    @classmethod
    def get_sorted_statuses(cls):
        statuses = StatusModel.query.all()
        statuses.sort(key=lambda status: status.sequence_num)
        return statuses
