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
        return OrderModel.query.all()

    # @ classmethod
    # def get_state(cls, state):
    #     return db.session.query.filter(OrderModel.state == state)

    @ classmethod
    def get_order_by_order_number(cls, order_number):
        orders = OrderModel.query.filter(OrderModel.order_number == order_number).first()
        return orders

    @ classmethod
    def get_coffice(cls, coffice):
        return OrderModel.query.filter(OrderModel.coffice == coffice)


