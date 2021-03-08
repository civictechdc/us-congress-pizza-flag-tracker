from models import OrderModel
from flask_sqlalchemy import sqlalchemy
from config import * #important for db


class OrderTransactions():
# Table actions:
    @classmethod
    def create(cls, usastate: str, order_number: int, coffice: str):
        new_order = OrderModel(usastate, order_number,coffice)
        db.session.add(new_order)
        db.session.commit()
        return new_order

   
    @ classmethod
    def get(cls):
        return OrderModel.query.all()

    @ classmethod
    def getstate(cls, state):
        return db.session.query.filter(OrderModel.state == state)

    @ classmethod
    def getorder(cls, order_number):
        orders = OrderModel.query.filter(OrderModel.order_number == order_number).all()
        return orders

    @ classmethod
    def getcoffice(cls, coffice):
        return OrderModel.query.filter(OrderModel.coffice == coffice)


