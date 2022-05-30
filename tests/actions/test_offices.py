import pytest
import datetime
import random
from src.office.office_actions import OfficeActions
from src.office.office_model import OfficeModel
from config import *


class TestOfficeActions:
    default_usa_state = "MA"
    default_office_code = default_usa_state + "-99"

    number_of_seconds_in_a_day = 24 * 60 * 60

    @pytest.mark.skip(reason="Need to figure out how to delete")
    def test_create(self):
        OfficeActions.delete(self.default_office_code)
        office = OfficeActions.create(
            usa_state=self.default_usa_state, office_code=self.default_office_code
        )
        actual_office_code = office.office_code
        actual_usa_state = office.usa_state
        total_seconds_since_created = (
            datetime.datetime.now() - office.created_at
        ).total_seconds()
        total_seconds_since_updated = (
            datetime.datetime.now() - office.updated_at
        ).total_seconds()
        assert actual_office_code == self.default_office_code
        assert actual_usa_state == self.default_usa_state
        assert total_seconds_since_created < 1
        assert total_seconds_since_updated < 1

    def test_can_get_populated_office(self):
        retrieved_office = OfficeActions.get_by_code("CA-02")
        assert retrieved_office.office_code == "CA-02"
        assert retrieved_office.usa_state == "CA"

    def test_get_offices(self):
        actual_offices = OfficeActions.get_offices()
        assert len(actual_offices) > 0
        firstOffice = actual_offices[0]
        assert (len(firstOffice["office_code"])) > 0

    # def test_controllers_get_office_by_uuid(self):
    #     unique_office_code = random.randint(1,1000000)
    #     created_office = OfficeActions.create( "OH",  unique_office_code , "OH06")
    #     actual_office=controllers_get_office_by_uuid(created_office.uuid)

    #     assert(actual_office['usa_state'] == "OH")
    #     assert(actual_office['office_code'] == "OH06")
    #     assert(actual_office['office_code'] == unique_office_code)
    #     assert(actual_office['uuid'] == created_office.uuid)

    # def test_update_office(self):
    #     unique_office_code = random.randint(1,1000000)
    #     created_office = OfficeActions.create( "OH",  unique_office_code , "OH06")
    #     actual_office=OfficeActions.get_office_by_uuid(created_office.uuid)

    #     usa_state = "VA"
    #     office_code = "031E"
    #     office_code = random.randint(1,1000000)
    #     uuid = actual_office.uuid
    #     updated_office = OfficeActions.update_office(uuid, usa_state, office_code , office_code)

    #     refreshed_actual_office=OfficeActions.get_office_by_uuid(created_office.uuid)
    #     assert(refreshed_actual_office.usa_state == usa_state)
    #     assert(refreshed_actual_office.office_code == office_code)
    #     assert(refreshed_actual_office.office_code == office_code)
