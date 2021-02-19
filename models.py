# ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from config import *

# id, State, Order Number, COffice, created_at , updated_at


class OrderModel(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(255))
    # order_number = db.Column(db.Integer,db.ForeignKey('order_number.id'),nullable = False)
    order_number = db.Column(db.Integer, nullable=False)

    coffice = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())
# Add relationships here when all teables have been created.

# Table actions:
    @classmethod
    def create(cls, usastate: str, order_number: int, coffice: str):
        # self.mystate = mystate
        # self.order_number = order_number
        # self.coffice = coffice
        # new_order = self(self)
        new_order = cls(state = usastate,
                          order_number = order_number,
                          coffice = coffice
                          )
        db.session.add(new_order)
        db.session.commit()
        return new_order

   
    @ classmethod
    def get(cls):
        return self.query.all()

    @ classmethod
    def getstate(cls, state):
        return db.session.query.filter(self.state == state)

    @ classmethod
    def getorder(cls, order_number):
        orders = cls.query.filter(cls.order_number == order_number).all()
        return orders

    @ classmethod
    def getcoffice(cls, coffice):
        return self.query.filter(self.coffice == coffice)
