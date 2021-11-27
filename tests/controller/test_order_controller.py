import random

import AuthController
import AuthPrivileges
from OrderActions import OrderActions
import OrderController
from tests.mock_request import mock_request
import tests.mock_auth_controller
import tests.mock_auth_privileges
import pytest

class TestOrderController():

    def test_controllers_get_order_by_uuid(self, mocker):
        mocker.patch.object(OrderController, AuthController.__name__,
                            tests.mock_auth_controller)
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH", unique_order_number, "OH06")
        actual_order = OrderController.get_order_by_uuid(created_order.uuid)

        assert (actual_order['usa_state'] == "OH")
        assert (actual_order['home_office_code'] == "OH06")
        assert (actual_order['order_number'] == str(unique_order_number))
        assert (actual_order['uuid'] == created_order.uuid)

    # @pytest.mark.skip(reason="Test fails because not mocked properly, skipping until fixed")
    def test_create_order(self, mocker):

        unique_order_number = random.randint(1, 100000000)

        order_request_json = {"usa_state": "OH", "home_office_code": "OH06", "order_number": unique_order_number}
        mock_request.mock_request_json = order_request_json;

        mocker.patch.object(OrderController, 'request', mock_request)
        mocker.patch.object(OrderController, AuthController.__name__, tests.mock_auth_controller)
        mocker.patch.object(OrderController, AuthPrivileges.__name__, tests.mock_auth_privileges)

        response = OrderController.create_order()
        assert (response['usa_state'] == "OH")
        assert (response['home_office_code'] == "OH06")
        assert (response['order_number'] == str(unique_order_number))
