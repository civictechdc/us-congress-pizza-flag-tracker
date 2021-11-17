from models import OrderModel, StatusModel
from config import db
import uuid


class OrderActions():
    @classmethod
<<<<<<< HEAD
    def create(cls, usa_state: str, order_number: int, home_office_code: str,
               order_status_id: int = None, order_status: OrderModel = None):
        theUuid = str(uuid.uuid4())
        new_order = OrderModel(
            theUuid, usa_state, order_number, home_office_code, order_status_id, order_status)
=======
    def create(cls, usa_state: str, order_number: int, home_office_code: str, order_status_id: int = 1):
        theUuid = str(uuid.uuid4())
        new_order = OrderModel(
            theUuid, usa_state, order_number, home_office_code, order_status_id)
>>>>>>> 66fd9f5 (rename order_status to order_status_id)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @ classmethod
    def get(cls):
        orders = OrderModel.query.all()
        return orders

    @ classmethod
<<<<<<< HEAD
    def get_order_by_order_number(cls, order_number):
=======
    def get_order_by_order_number_as_tuple(cls, order_number):
>>>>>>> 66fd9f5 (rename order_status to order_status_id)
        order = OrderModel.query.filter(
            OrderModel.order_number == order_number).first()
        return order

    @ classmethod
    def get_order_by_uuid(cls, uuid):
        order = OrderModel.query.filter(OrderModel.uuid == uuid).first()
        return order

    @ classmethod
    def get_by_home_office_code(cls, home_office_code):
        return OrderModel.query.filter(OrderActions.home_office_code == home_office_code)

    @ classmethod
    def update_order_by_uuid(cls, uuid, usa_state=None, order_number=None, home_office_code=None, order_status_id=None):
<<<<<<< HEAD
        order = cls.get_order_by_uuid(uuid)
        order.order_number = order_number or order.order_number
        order.usa_state = usa_state or order.usa_state
        order.home_office_code = home_office_code or order.home_office_code
        order.order_status_id = order_status_id or order.order_status_id
=======
        order: OrderActions = cls.get_order_by_uuid(uuid)
        order.update_order(usa_state, order_number,
                           home_office_code, order_status_id)
>>>>>>> 66fd9f5 (rename order_status to order_status_id)
        db.session.commit()
        return order
