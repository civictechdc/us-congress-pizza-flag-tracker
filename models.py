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
    
    #uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # uuid = db.Column(db.Integer, db.ForeignKey('order_number.id'), nullable = False)
 
    order_number = db.Column(db.Integer, nullable=False)

    coffice = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, state, order_number, coffice):
       self.state = state
       self.order_number = order_number
       self.coffice = coffice
