import json
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from src.constituent.constituent_model import ConstituentModel
from config import db
import uuid

from src.util import table_record_to_json, table_to_json


def xyz(keyword, constituent):
    return keyword in json.dumps(table_record_to_json(constituent))


class ConstituentQueryParams:
    statuses = ""
    name = ""
    office_code = ""
    keyword = ""

    def isEmpty(self):
        return not (self.status_code or self.name or self.office_code)


class ConstituentActions:
    @classmethod
    def create(
        cls,
        name: str,
        address: int,
        town: str,
        phone: str,
        uuid_param: str = None,
    ):
        theUuid = uuid_param or str(uuid.uuid4())
        new_constituent = ConstituentModel(
            theUuid,
            name,
            address,
            town,
            phone,
        )
        db.session.add(new_constituent)
        db.session.commit()
        return new_constituent

    @classmethod
    def get_constituents(
        cls, query_params: ConstituentQueryParams = ConstituentQueryParams()
    ):
        constituents = ConstituentModel.query.all()

        return constituents

    @classmethod
    def get_constituent_by_uuid(cls, uuid):
        constituent = ConstituentModel.query.filter(
            ConstituentModel.uuid == uuid
        ).first()
        return constituent
