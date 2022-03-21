import random

from src.auth import auth_controller, auth_privileges
from src.order.order_actions import OrderActions
from src.order import order_controller
from src.status.status_actions import StatusActions
from tests.mock_request import mock_request
import tests.mock_auth_controller
import tests.mock_auth_privileges
import pytest

from src.util import table_record_to_json


class TestOrderController():

    def test_controllers_get_order_by_uuid(self, mocker):
        # TODO refactor this to auth_controller.__name__
        mocker.patch.object(order_controller, "auth_controller",  #auth_controller.__name__,
                            tests.mock_auth_controller)
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH", unique_order_number, "OH06")
        actual_order = order_controller.get_order_by_uuid(created_order.uuid)

        assert (actual_order['usa_state'] == "OH")
        assert (actual_order['home_office_code'] == "OH06")
        assert (actual_order['order_number'] == str(unique_order_number))
        assert (actual_order['uuid'] == created_order.uuid)

    # @pytest.mark.skip(reason="Test fails because not mocked properly, skipping until fixed")
    def test_create_update_order(self, mocker):

        mocker.patch.object(order_controller, 'request', mock_request)
        # TODO refactor this to auth_controller.__name__
        mocker.patch.object(order_controller, "auth_controller",  #auth_controller.__name__,
                            tests.mock_auth_controller)
        mocker.patch.object(order_controller, "auth_privileges", tests.mock_auth_privileges)

        unique_order_number = random.randint(1, 100000000)
        status = StatusActions.get_statuses()[2]
        order_request_json = {"usa_state": "OH", "home_office_code": "OH06",
                              "order_number": unique_order_number, "order_status_id":status.id}
        mock_request.mock_request_json = order_request_json;


        response = order_controller.create_order()

        TestOrderController.assertExpectedOrder(order_request_json, response, status)

        status = StatusActions.get_statuses()[2]
        order_request_json = {"usa_state": "MA", "home_office_code": "MA06",
                              "order_number": unique_order_number+1, "order_status_id":status.id}
        mock_request.mock_request_json = order_request_json;

        response = order_controller.update_order(uuid=response['uuid'])

        TestOrderController.assertExpectedOrder(order_request_json, response, status)


    @staticmethod
    def assertExpectedOrder(order_request_json, response, status):
        assert (response['usa_state'] == order_request_json['usa_state'])
        assert (response['home_office_code'] == order_request_json['home_office_code'])
        assert (response['order_number'] == str(order_request_json['order_number']))
        assert (response['status']['description']) == status.description;
        order = OrderActions.get_order_by_uuid(response['uuid']);
        assert (order.usa_state == order_request_json['usa_state'])
        assert (order.home_office_code == order_request_json['home_office_code'])
        assert (order.order_number == order_request_json['order_number'])
        assert (order.status.description) == status.description;





