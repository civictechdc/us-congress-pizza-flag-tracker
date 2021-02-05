#ORM models for State, Order, User and Log db
from flask_sqlalchemy import sqlalchemy
from flask_migrate import Migrate
from sqlalchemy import func
from config import *

#id, State, Order Number, COffice, created_at , updated_at
class Order(db.Model):
    __tablename__="orders"
    id=db.Column(db.Integer,primary_key=True)
    state = db.Column(db.String(255))
    order_number = db.Column(db.Integer,db.ForeignKey('order_number.id'),nullable = False)
    coffice = db.Column(db.String(255))
    created_at = db.Column(db.DateTime,server_default = func.now())
    updated_at = db.Column(db.DateTime,server_default = func.now(), onupdate=func.now())
#Add relationships here when all teables have been created.   

#Table actions: 
    @classmethod
    def new(state:str, order_number:int ,coffice:str):
        self.state = state
        self.order_number = order_number
        self.coffice = coffice
        new_order = self(state,order_number,coffice)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @classmethod
    def get():
        return self.query.all()

    @classmethod
    def getstate(state):
        return self.query.filter(self.state == state)
        
    @classmethod
    def getorder(order_number):
        return self.query.filter(self.order_number == order_number)

    @classmethod
    def getcoffice(coffice):
        return self.query.filter(self.coffice == coffice)

