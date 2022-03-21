import random

from src.order.order_actions import OrderActions
from src.user import user_controller
from src.status.status_actions import StatusActions
from tests.mock_request import mock_request
import tests.mock_auth_controller
import tests.mock_auth_privileges
import pytest

from src.util import table_record_to_json


class TestUserController():

    # def test_controllers_get_order_by_uuid(self, mocker):
    #     # TODO refactor this to auth_controller.__name__
    #     mocker.patch.object(order_controller, "auth_controller",  #auth_controller.__name__,
    #                         tests.mock_auth_controller)
    #     unique_order_number = random.randint(1, 1000000)
    #     created_order = OrderActions.create("OH", unique_order_number, "OH06")
    #     actual_order = order_controller.get_order_by_uuid(created_order.uuid)

    #     assert (actual_order['usa_state'] == "OH")
    #     assert (actual_order['home_office_code'] == "OH06")
    #     assert (actual_order['order_number'] == str(unique_order_number))
    #     assert (actual_order['uuid'] == created_order.uuid)

    # @pytest.mark.skip(reason="Test fails because not mocked properly, skipping until fixed")
    def test_create_update_user(self, mocker):

        mocker.patch.object(user_controller, 'request', mock_request)
        # TODO refactor this to auth_controller.__name__
        mocker.patch.object(user_controller, "auth_controller",  #auth_controller.__name__,
                            tests.mock_auth_controller)
        mocker.patch.object(user_controller, "auth_privileges", tests.mock_auth_privileges)

        unique_user_number = str(random.randint(1, 100000000))
        user_request_json = { "username": "TEST-ADMIN"+unique_user_number, "password": "abcd", "office_code": "FED-ADMIN",
                              "manage_all_orders": "Y", "update_all_statuses": "Y", "view_all_orders": "Y",
                              "manage_all_users": "Y", "manage_office_users": "Y", "update_own_password": "Y",
                              "can_create_update_delete_orders": "Y", "can_update_status_for": "ALL", "can_update_password_for": "ALL", "is_admin": "Y"
        }

        mock_request.mock_request_json = user_request_json


        response = user_controller.create_user()

        TestUserController.assertExpectedUser(user_request_json, response)

        # order_request_json = {"usa_state": "MA", "home_office_code": "MA06",
        #                       "order_number": unique_order_number+1, "order_status_id":status.id}
        # mock_request.mock_request_json = order_request_json;

        # response = order_controller.update_order(uuid=response['uuid'])

        # TestOrderController.assertExpectedOrder(order_request_json, response, status)


    @staticmethod
    def assertExpectedUser(user_request_json, response):
        if type(response) is tuple:
            response_data = response[0]
        else:
            response_data = response
        assert (response_data['username'] == user_request_json['username'])






