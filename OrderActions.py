from models import OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid

class OrderActions():
# Table actions:
    @classmethod
    def create(cls, usastate: str, order_number: int, home_office_code: str, order_status:int):
        theUuid = str(uuid.uuid4())
        new_order = OrderModel(theUuid, usastate, order_number,home_office_code,order_status)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @ classmethod
    def get(cls):
        orders = OrderModel.query.all()
        return {"orders": [{"order_number": i.order_number, "uuid": i.uuid, "usa_state": i.usa_state, "home_office_code": i.home_office_code} 
          for i in orders]}

    # @ classmethod
    # def get_state(cls, state):
    #     return db.session.query.filter(OrderModel.state == state)

    @ classmethod
    def get_order_by_order_number(cls, order_number):
        order = OrderModel.query.filter(OrderModel.order_number == order_number).first()
        return order

    @ classmethod
    def get_order_by_uuid(cls, uuid):
        # Return OrderModel object for use by backend
        order = OrderModel.query.filter(OrderModel.uuid == uuid).first()
        return order

    @ classmethod
    def get_home_office_code(cls, home_office_code):
        return OrderModel.query.filter(OrderModel.home_office_code == home_office_code)

    @ classmethod
    def update_order(cls, uuid, usa_state, order_number , home_office_code):
        order = cls.get_order_by_uuid(uuid)
        order.order_number = order_number
        order.usa_state = usa_state
        order.home_office_code = home_office_code 
        db.session.commit()
        return order
     
