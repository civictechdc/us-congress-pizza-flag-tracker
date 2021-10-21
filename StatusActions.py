from models import StatusModel, OfficeModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid


class StatusActions:
    # Table actions:

    @classmethod
    def get_statuses(cls):
        statuses = StatusModel.query.all()
        return [
            {
                "status_federal_office_code": status.status_federal_office_code,
                "sequence_num": status.sequence_num,
                "description": status.description,
                "created_at": status.created_at,
                "updated_at": status.updated_at
            }
            for status in statuses
        ]
