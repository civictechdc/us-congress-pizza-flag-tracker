from models import OrderModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid

class OrderActions():
# Table actions:
    @classmethod
    def create(cls, usastate: str, order_number: int, coffice: str):
        theUuid = str(uuid.uuid4())
        new_order = OrderModel(theUuid, usastate, order_number,coffice)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @ classmethod
    def get(cls):
        orders = OrderModel.query.all()
        return {"orders": [{"order_number": i.order_number, "uuid": i.uuid, "usa_state": i.usa_state, "coffice": i.coffice} 
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
    def get_coffice(cls, coffice):
        return OrderModel.query.filter(OrderModel.coffice == coffice)

    @ classmethod
    def update_order(cls, uuid, usa_state, order_number , coffice):
        order = cls.get_order_by_uuid(uuid)
        order.order_number = order_number
        order.usa_state = usa_state
        order.coffice = coffice 
        db.session.commit()
        return order
     
