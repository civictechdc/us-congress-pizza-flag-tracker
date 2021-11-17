from models import StatusModel, OfficeModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid


class StatusActions:
    # Table actions:

    @classmethod
    def get_statuses(cls):
        return StatusModel.query.all()
