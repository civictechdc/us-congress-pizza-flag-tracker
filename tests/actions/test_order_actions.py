import random
from src.order.order_actions import OrderActions
from StatusActions import StatusActions
from models import StatusModel
from src.order.order_models import OrderModel


class TestOrderActions():

    def test_create(self):
        unique_order_number = random.randint(1, 1000000)
        expected_status: StatusModel = StatusActions.get_statuses()[0]
        status_id = expected_status.id
        OrderActions.create(
            usa_state="MD",  order_number=unique_order_number, home_office_code="MD06",
            order_status_id=status_id)
        retrievedOrder: OrderModel = OrderActions.get_order_by_order_number(
            unique_order_number)
        assert(retrievedOrder.order_number == unique_order_number)
        assert(retrievedOrder.order_status_id == status_id)
        assert(retrievedOrder.status == expected_status)

    def test_unique_uuid(self):
        unique_order_number1 = random.randint(1, 1000000)
        unique_order_number2 = random.randint(1, 1000000)
        OrderActions.create("MD", unique_order_number1, "MD06")
        order1 = OrderActions.get_order_by_order_number(
            unique_order_number1)
        OrderActions.create("MA", unique_order_number2, "MA08")
        order2 = OrderActions.get_order_by_order_number(
            unique_order_number2)
        assert(order1.uuid != order2.uuid)

    def test_get_orders(self):
        unique_order_number = random.randint(1, 1000000)
        order = OrderActions.create("MD",  unique_order_number, "MD06")
        get_orders = OrderActions.get()
        found = False

        for order in get_orders:
            if order.order_number == unique_order_number:
                found = True
        assert(found)

    def test_get_order(self):
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("MD",  unique_order_number, "MD06")
        actual_order = OrderActions.get_order_by_order_number(
            created_order.order_number)

        assert(actual_order.usa_state == "MD")
        assert(actual_order.home_office_code == "MD06")
        assert(actual_order.order_number == unique_order_number)

    def test_get_order_by_uuid(self, mocker):
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH",  unique_order_number, "OH06")
        actual_order = OrderActions.get_order_by_uuid(created_order.uuid)

        assert(actual_order.usa_state == "OH")
        assert(actual_order.home_office_code == "OH06")
        assert(actual_order.order_number == unique_order_number)
        assert(actual_order.uuid == created_order.uuid)

    def test_update_order(self):
        unique_order_number = random.randint(1, 1000000)
        created_order = OrderActions.create("OH",  unique_order_number, "OH06")
        actual_order = OrderActions.get_order_by_uuid(created_order.uuid)

        usa_state = "VA"
        home_office_code = "031E"
        order_number = random.randint(1, 1000000)
        uuid = actual_order.uuid
        OrderActions.update_order_by_uuid(
            uuid, usa_state, order_number, home_office_code)

        refreshed_actual_order = OrderActions.get_order_by_uuid(
            created_order.uuid)
        assert(refreshed_actual_order.usa_state == usa_state)
        assert(refreshed_actual_order.home_office_code == home_office_code)
        assert(refreshed_actual_order.order_number == order_number)
