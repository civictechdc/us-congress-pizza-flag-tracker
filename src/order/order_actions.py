from src.status.status_model import StatusModel
from src.order.order_model import OrderModel
from config import db
import uuid


class OrderActions:
    @classmethod
    def create(
        cls,
        usa_state: str,
        order_number: int,
        home_office_code: str,
        order_status_id: int = None,
        order_status: OrderModel = None,
    ):
        theUuid = str(uuid.uuid4())
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
        return new_order

    @classmethod
    def get(cls,office):
        if office == 'FED':
            orders = OrderModel.query.all()
        else:
            orders = OrderModel.query.filter(OrderModel.home_office_code == office)
        return orders

    @classmethod
    def get_order_by_order_number(cls, order_number):
        order = OrderModel.query.filter(OrderModel.order_number == order_number).first()
        return order

    @classmethod
    def get_order_by_uuid(cls, uuid):
        order = OrderModel.query.filter(OrderModel.uuid == uuid).first()
        return order

    @classmethod
    def get_by_home_office_code(cls, home_office_code):
        return OrderModel.query.filter(
            OrderActions.home_office_code == home_office_code
        )

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
        db.session.commit()
        return order

    @classmethod
    def delete_order_by_uuid(cls, uuid):
        order = cls.get_order_by_uuid(uuid)
        db.session.delete(order)
        db.session.commit()
        return "Deleted", 204

    @classmethod
    def commit_status_update(cls):
        db.session.commit()
        return
