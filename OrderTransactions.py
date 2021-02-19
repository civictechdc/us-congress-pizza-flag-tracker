from models import OrderModel
from flask_sqlalchemy import sqlalchemy
from config import * #important for db


class OrderTransactions():
    @classmethod
    def create(cls, usastate: str, order_number: int, coffice: str):
 
        #TODO: Move the method create to here from model.py
        #  and reference OrderModel indirectly using the import.
        new_order = OrderModel.create(usastate = usastate, order_number = order_number, coffice = coffice)

        return new_order


