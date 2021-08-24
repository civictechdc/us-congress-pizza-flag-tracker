import pytest
import datetime
import random
from OfficeActions import OfficeActions 
from models import OfficeModel
from config import *

class TestOfficeActions():
    default_usa_state = "MA"
    default_office_code = default_usa_state + "-18"
    default_office_name = "Office "+default_office_code
    default_usa_state2 = "NH"
    default_office_code2 = default_usa_state2 + "-03"
    default_office_name2 = "Office "+default_office_code2
    number_of_seconds_in_a_day = 24*60*60
    
    def setup_method(self, method):
        print("setup")
        OfficeActions.delete()

    def test_create(self):
        office = OfficeActions.create(
            usa_state = self.default_usa_state, 
            office_code=self.default_office_code, 
            office_name=self.default_office_name
        )
        total_seconds_since_created = (datetime.datetime.now()-office.created_at).total_seconds()
        total_seconds_since_updated = (datetime.datetime.now()-office.updated_at).total_seconds()
        assert office.office_code == self.default_office_code 
        assert(office.usa_state == self.default_usa_state)        
        assert(office.office_name == self.default_office_name)   
        assert (total_seconds_since_created < 1)

    def test_get_given_office_created_(self):
        OfficeActions.create(
            office_code=self.default_office_code, 
            usa_state = self.default_usa_state, 
            office_name= self.default_office_name
        )
        retrieved_office = OfficeActions.get_by_code(office_code=self.default_office_code)
        assert(retrieved_office.office_code == self.default_office_code)        
        assert(retrieved_office.usa_state == self.default_usa_state)        
        assert(retrieved_office.office_name == self.default_office_name)

    def test_get_offices(self):
        OfficeActions.create(
            usa_state = self.default_usa_state, 
            office_code=self.default_office_code, 
            office_name=self.default_office_name
        )
        OfficeActions.create(
            usa_state = self.default_usa_state2, 
            office_code=self.default_office_code2, 
            office_name=self.default_office_name2
        )
        found = False
        actual_offices = OfficeActions.get_offices()["offices"]
        for office in actual_offices:
            if office["office_code"] == self.default_office_code2:
                found = True
                assert(office["office_code"] == self.default_office_code2)        
                assert(office["usa_state"] == self.default_usa_state2)        
                assert(office["office_name"] == self.default_office_name2)
        assert(found)

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

