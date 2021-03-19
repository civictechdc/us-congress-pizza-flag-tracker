# ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from config import *

# id, State, Order Number, COffice, created_at , updated_at

class OrderModel(db.Model):
    __tablename__ = "orders"
    order_number = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(255))
    coffice = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, theUuid, usa_state, order_number, coffice):
       self.usa_state = usa_state
       self.order_number = order_number
       self.coffice = coffice
       self.uuid = theUuid
