import pytest
import random
from OrderActions import OrderActions 
import OrderController
from OrderController import get_order_by_uuid as controllers_get_order_by_uuid
import authorize


class TestOrderController():

    @staticmethod
    def mock_function():
        pass

    def test_controllers_get_order_by_uuid(self, mocker):
        mocker.patch.object(OrderController, 'raise_exception_if_invalid_token_else_set_current_user', TestOrderController.mock_function)
        unique_order_number = random.randint(1,1000000)
        created_order = OrderActions.create( "OH",  unique_order_number , "OH06")
        actual_order=controllers_get_order_by_uuid(created_order.uuid)
        
        assert(actual_order['usa_state'] == "OH")
        assert(actual_order['home_office_code'] == "OH06")
        assert(actual_order['order_number'] == unique_order_number)
        assert(actual_order['uuid'] == created_order.uuid)       


