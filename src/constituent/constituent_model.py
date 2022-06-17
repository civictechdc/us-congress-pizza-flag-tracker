from config import db
from sqlalchemy import func
from sqlalchemy.sql.expression import join


class ConstituentModel(db.Model):

    #     "name": mock_constituent[0],
    # "Constituent": mock_constituent[1],
    # "town": mock_constituent[2]
    # + ", "
    # + constituent_dict["name"]
    # + " "
    # + mock_constituent[3],
    # "phone": mock_constituent[4],
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
