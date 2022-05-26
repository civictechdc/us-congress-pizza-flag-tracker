from src.status.status_model import StatusModel
from src.order.order_model import OrderModel
from src.order_log.order_log_actions import LogActions
from config import db
import uuid


class OrderQueryParams:
    status_code = ""
    state = ""
    office_code = ""

    def isEmpty(self):
        return not (self.status_code or self.state or self.office_code)


class OrderActions:
    @classmethod
    def create(
        cls,
        usa_state: str,
        order_number: int,
        home_office_code: str,
        order_status_id: int = None,
        order_status: OrderModel = None,
        uuid_param: str = None,
    ):
        theUuid = uuid_param or str(uuid.uuid4())
        new_order = OrderModel(
            theUuid,
            usa_state,
            order_number,
            home_office_code,
            order_status_id,
            order_status,
        )
        db.session.add(new_order)
        db.session.commit()
        LogActions.create_order_log(
            theUuid, usa_state, order_number, home_office_code, order_status_id
        )
        return new_order

    @classmethod
    def get_orders(cls, query_params: OrderQueryParams = OrderQueryParams()):
        query = OrderModel.home_office_code == OrderModel.home_office_code
        if query_params.office_code:
            query = query & (OrderModel.home_office_code ==
                             query_params.office_code)
        orders = OrderModel.query.filter(query)
        return [order for order in orders]

    @classmethod
    def get_order_by_order_number(cls, order_number):
        order = OrderModel.query.filter(
            OrderModel.order_number == order_number).first()
        return order

    @classmethod
    def get_order_by_uuid(cls, uuid):
        order = OrderModel.query.filter(OrderModel.uuid == uuid).first()
        return order

    # Do we need this classmethod?
    @classmethod
    def get_by_home_office_code(cls, home_office_code):
        return OrderModel.query.filter(
            OrderActions.home_office_code == home_office_code
        )

    @classmethod
    def get_orders_by_usa_state(cls, usa_state):
        return OrderModel.query.filter(OrderActions.usa_state == usa_state)

    @classmethod
    def get_orders_by_order_status_id(cls, order_status_id):
        return OrderModel.query.filter(OrderActions.order_status_id == order_status_id)

    @classmethod
    def update_order_by_uuid(
        cls,
        uuid,
        usa_state=None,
        order_number=None,
        home_office_code=None,
        order_status_id=None,
    ):
        order = cls.get_order_by_uuid(uuid)
        order.order_number = order_number or order.order_number
        order.usa_state = usa_state or order.usa_state
        order.home_office_code = home_office_code or order.home_office_code
        order.order_status_id = order_status_id or order.order_status_id
        LogActions.create_order_log(
            uuid, order.usa_state, order.order_number, order.home_office_code, order.order_status_id
        )
        db.session.commit()
        return order

    @classmethod
    def delete_order_by_uuid(cls, uuid):
        order = cls.get_order_by_uuid(uuid)
        db.session.delete(order)
        db.session.commit()

    @classmethod
    def commit_status_update(cls):
        db.session.commit()
        return
