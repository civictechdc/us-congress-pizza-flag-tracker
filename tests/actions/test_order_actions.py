from itertools import count
import random
from numpy import size

from pytz import NonExistentTimeError
from src.order.order_actions import OrderActions, OrderQueryParams
from src.status.status_actions import StatusActions
from src.status.status_model import StatusModel
from src.order.order_model import OrderModel


class TestOrderActions:
    def test_create(self):
        unique_order_number = random.randint(1, 1000000)
        expected_status: StatusModel = StatusActions.get_sorted_statuses()[0]
        status_id = expected_status.id
        OrderActions.create(
            usa_state="MD",
            order_number=unique_order_number,
            home_office_code="MD06",
            order_status_id=status_id,
        )
        retrievedOrder: OrderModel = OrderActions.get_order_by_order_number(
            unique_order_number
        )
        assert retrievedOrder.order_number == unique_order_number
        assert retrievedOrder.order_status_id == status_id
        assert retrievedOrder.status == expected_status

    def test_unique_uuid(self):
        unique_order_number1 = random.randint(1, 1000000)
        unique_order_number2 = random.randint(1, 1000000)
        OrderActions.create("MD", unique_order_number1, "MD06")
        order1 = OrderActions.get_order_by_order_number(unique_order_number1)
        OrderActions.create("MA", unique_order_number2, "MA08")
        order2 = OrderActions.get_order_by_order_number(unique_order_number2)
        assert order1.uuid != order2.uuid

    def test_get_orders_by_office_code(self):
        office_to_query = "MD-06"
        unique_order_number = random.randint(1, 1000000)
        order = OrderActions.create("MD", unique_order_number, office_to_query)
        unique_order_number2 = random.randint(1, 1000000)
        order = OrderActions.create("CA", unique_order_number2, "CA-03")
        query_params = OrderQueryParams()
        query_params.office_code = office_to_query
        found_orders = OrderActions.get_orders(query_params)
        assert len(found_orders) > 0

        for order in found_orders:
            error_msg = (
                "Should not have found "
                + str(order.order_number)
                + " "
                + order.home_office_code
            )
            assert order.home_office_code == query_params.office_code, error_msg

    def test_get_orders_by_usa_state(self):
        state_to_query = "MD"
        unique_order_number = random.randint(1, 1000000)
        order = OrderActions.create(
            usa_state=state_to_query,
            order_number=unique_order_number,
            home_office_code="MD-06",
        )
        unique_order_number2 = random.randint(1, 1000000)
        order = OrderActions.create(
            usa_state="CA", order_number=unique_order_number2, home_office_code="CA-03"
        )
        query_params = OrderQueryParams()
        query_params.usa_state = state_to_query
        found_orders = OrderActions.get_orders(query_params)
        assert len(found_orders) > 0

        for order in found_orders:
            assert order.usa_state == query_params.usa_state

    def test_get_orders_by_single_status_code(self):
        statuses = StatusActions.get_sorted_statuses()
        status_to_query = statuses[1].status_code
        unique_order_number = random.randint(1, 1000000)
        usa_state = "MD"
        home_office_code = "MD-06"
        order = OrderActions.create(
            usa_state=usa_state,
            order_number=unique_order_number,
            home_office_code=home_office_code,
        )
        order = OrderActions.update_order_by_uuid(
            order.uuid, order_status_id=statuses[1].id
        )
        unique_order_number2 = random.randint(1, 1000000)
        order = OrderActions.create(
            usa_state="CA", order_number=unique_order_number2, home_office_code="CA-03"
        )
        query_params = OrderQueryParams()
        query_params.statuses = status_to_query
        found_orders = OrderActions.get_orders(query_params)

        assert len(found_orders) > 0

        for order in found_orders:
            assert order.order_status_id == statuses[1].id

    def test_get_order_by_order_number(self):
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("MD", unique_order_number, "MD06")
        actual_order = OrderActions.get_order_by_order_number(
            created_order.order_number
        )
        assert actual_order.usa_state == "MD"
        assert actual_order.home_office_code == "MD06"
        assert actual_order.order_number == unique_order_number

    def test_get_order_by_uuid(self, mocker):
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH", unique_order_number, "OH06")
        actual_order = OrderActions.get_order_by_uuid(created_order.uuid)

        assert actual_order.usa_state == "OH"
        assert actual_order.home_office_code == "OH06"
        assert actual_order.order_number == unique_order_number
        assert actual_order.uuid == created_order.uuid

    def test_update_order(self):
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH", unique_order_number, "OH06")
        actual_order = OrderActions.get_order_by_uuid(created_order.uuid)

        usa_state = "VA"
        home_office_code = "031E"
        order_number = random.randint(1, 1000000)
        uuid = actual_order.uuid
        OrderActions.update_order_by_uuid(
            uuid, usa_state, order_number, home_office_code
        )

        refreshed_actual_order = OrderActions.get_order_by_uuid(created_order.uuid)
        assert refreshed_actual_order.usa_state == usa_state
        assert refreshed_actual_order.home_office_code == home_office_code
        assert refreshed_actual_order.order_number == order_number

    def test_get_orders_by_multiple_status_code(self):
        statuses = StatusActions.get_sorted_statuses()
        status_to_query = statuses[1].status_code + \
            ", " + statuses[2].status_code
        unique_order_number = random.randint(1, 1000000)
        usa_state = "MD"
        home_office_code = "MD-06"

        order = OrderActions.create(
            usa_state=usa_state, order_number=unique_order_number, home_office_code=home_office_code)
        order = OrderActions.update_order_by_uuid(
            order.uuid, order_status_id=statuses[1].id)

        unique_order_number2 = random.randint(1, 1000000)
        order = OrderActions.create(
            usa_state=usa_state, order_number=unique_order_number2, home_office_code=home_office_code)
        order = OrderActions.update_order_by_uuid(
            order.uuid, order_status_id=statuses[2].id)

        unique_order_number3 = random.randint(1, 1000000)
        order = OrderActions.create(
            usa_state="CA", order_number=unique_order_number3, home_office_code="CA-03")
        query_params = OrderQueryParams()
        query_params.statuses = status_to_query
        found_orders = OrderActions.get_orders(query_params)

        assert len(found_orders) > 0
        count_status1 = 0
        count_status2 = 0
        count_wrong_status = 0

        for order in found_orders:
            if statuses[1].id == order.order_status_id:
                count_status1 += 1
            elif statuses[2].id == order.order_status_id:
                count_status2 += 1
            else:
                count_wrong_status += 1

        assert count_status1 > 0 and count_status2 > 0 and count_wrong_status == 0
