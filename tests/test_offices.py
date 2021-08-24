import pytest
import random
from OfficeActions import OfficeActions 
from models import OfficeModel
from config import *

class TestOfficeActions():
    
    def test_create_and_get(self):
        print("Hello 2")
        office_code = "MA-12"
        office = OfficeActions.create(office_code=office_code, usa_state = "MA", office_name="Office 16")
        retrievedOffice = OfficeActions.get_by_code(office_code=office_code)
        assert(retrievedOffice.office_code == office_code)        

    def test_unique_uuid(self):
        unique_office_code1 = random.randint(1,1000000)
        unique_office_code2 = random.randint(1,1000000)
        OfficeActions.create("MD", unique_office_code1, "MD06")
        OfficeActions.create("MA", unique_office_code2, "MA08")

        office1 = OfficeActions.get_office_by_office_code(unique_office_code1)
        office2 = OfficeActions.get_office_by_office_code(unique_office_code2)
        assert(office1.uuid != office2.uuid)

    def test_get_offices(self):
        unique_office_code = random.randint(1,1000000)
        office = OfficeActions.create( "MD",  unique_office_code , "MD06")
        get_offices=OfficeActions.get()["offices"]
        found = False

        for office in get_offices:
            if office["office_code"] == unique_office_code:
                found = True
        assert(found)

    def test_get_office(self):
        unique_office_code = random.randint(1,1000000)
        created_office = OfficeActions.create( "MD",  unique_office_code , "MD06")
        actual_office=OfficeActions.get_office_by_office_code(created_office.office_code)
        
        assert(actual_office.usa_state == "MD")
        assert(actual_office.office_code == "MD06")
        assert(actual_office.office_code == unique_office_code)

    def test_get_office_by_uuid(self):
        unique_office_code = random.randint(1,1000000)
        created_office = OfficeActions.create( "OH",  unique_office_code , "OH06")
        actual_office=OfficeActions.get_office_by_uuid(created_office.uuid)
        
        assert(actual_office.usa_state == "OH")
        assert(actual_office.office_code == "OH06")
        assert(actual_office.office_code == unique_office_code)
        assert(actual_office.uuid == created_office.uuid)

    def test_controllers_get_office_by_uuid(self):
        unique_office_code = random.randint(1,1000000)
        created_office = OfficeActions.create( "OH",  unique_office_code , "OH06")
        actual_office=controllers_get_office_by_uuid(created_office.uuid)
        
        assert(actual_office['usa_state'] == "OH")
        assert(actual_office['office_code'] == "OH06")
        assert(actual_office['office_code'] == unique_office_code)
        assert(actual_office['uuid'] == created_office.uuid)       

    def test_update_office(self):
        unique_office_code = random.randint(1,1000000)
        created_office = OfficeActions.create( "OH",  unique_office_code , "OH06")
        actual_office=OfficeActions.get_office_by_uuid(created_office.uuid)

        usa_state = "VA"
        office_code = "031E"
        office_code = random.randint(1,1000000)
        uuid = actual_office.uuid
        updated_office = OfficeActions.update_office(uuid, usa_state, office_code , office_code)

        refreshed_actual_office=OfficeActions.get_office_by_uuid(created_office.uuid)
        assert(refreshed_actual_office.usa_state == usa_state)
        assert(refreshed_actual_office.office_code == office_code)
        assert(refreshed_actual_office.office_code == office_code)

