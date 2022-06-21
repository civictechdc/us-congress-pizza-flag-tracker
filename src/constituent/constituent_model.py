from config import db
from sqlalchemy import func
from sqlalchemy.sql.expression import join


class ConstituentModel(db.Model):
    __tablename__ = "constituents"
    uuid = db.Column(db.String(40), primary_key=True, index=True, nullable=False)
    name = db.Column(db.String(40))
    address = db.Column(db.String(40))
    town = db.Column(db.String(40))
    phone = db.Column(db.String(40))
    orders = db.relationship("OrderModel", back_populates="person")

    def __init__(
        self,
        theUuid,
        name,
        address,
        town,
        phone,
    ):
        self.uuid = theUuid
        self.name = name
        self.address = address
        self.town = town
        self.phone = phone
