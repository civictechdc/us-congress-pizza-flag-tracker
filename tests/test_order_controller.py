import random
from OrderActions import OrderActions
import OrderController
from OrderController import get_order_by_uuid as controllers_get_order_by_uuid, create_order
from tests.mock_request import mock_request
from tests.mocking_helper import MockingHelper


class TestOrderController():

    def test_controllers_get_order_by_uuid(self, mocker):
        mocker.patch.object(OrderController, OrderController.set_authorize_current_user.__name__,
                            MockingHelper.mock_static_or_regular_function)
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH", unique_order_number, "OH06")
        actual_order = controllers_get_order_by_uuid(created_order.uuid)

        assert (actual_order['usa_state'] == "OH")
        assert (actual_order['home_office_code'] == "OH06")
        assert (actual_order['order_number'] == unique_order_number)
        assert (actual_order['uuid'] == created_order.uuid)

    def test_create_order(self, mocker):
        unique_order_number = random.randint(1, 1000000)

        order_request_json = {"usa_state": "OH", "home_office_code": "OH06", "order_number": unique_order_number}
        mock_request.mock_request_json = order_request_json;
        mocker.patch.object(OrderController, 'request', mock_request)

        mocker.patch.object(OrderController, OrderController.set_authorize_current_user.__name__,
                            MockingHelper.mock_static_or_regular_function)
        mocker.patch.object(OrderController, OrderController.get_exception_if_no_create_update_delete_orders.__name__,
                            MockingHelper.mock_static_or_regular_function)

        response = create_order()
        assert (response['usa_state'] == "OH")
        assert (response['home_office_code'] == "OH06")
        assert (response['order_number'] == str(unique_order_number))
