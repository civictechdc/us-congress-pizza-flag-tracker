from config import db
from src.office.office_model import OfficeModel
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join


class OrderModel(db.Model):
    __tablename__ = "orders"
    order_number = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    usa_state = db.Column(db.String(10))
    # sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class OfficeModel->offices'. Original exception was: Could not determine join condition between parent/child tables on relationship OfficeModel.orders - there are multiple foreign key paths linking the tables.  Specify the 'foreign_keys' argument, providing a list of those columns which should be counted as containing a foreign key reference to the parent table.
    order_status_id = db.Column(db.Integer, db.ForeignKey("status.id"))
    constituent_id = db.Column(db.Integer, db.ForeignKey("constituents.uuid"))
    home_office_code = db.Column(db.String(10), db.ForeignKey(OfficeModel.office_code))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    status = db.relationship("StatusModel", back_populates="orders")
    person = db.relationship("ConstituentModel", back_populates="orders")

    def __init__(
        self,
        theUuid,
        usa_state,
        order_number,
        home_office_code,
        order_status_id,
        order_status=None,
        constituent_id=None,
    ):
        self.uuid = theUuid
        self.usa_state = usa_state
        self.order_number = order_number
        self.home_office_code = home_office_code
        self.constituent_id = constituent_id
        if order_status_id:
            self.order_status_id = order_status_id
        elif order_status:
            self.order_status_id = order_status.id

    def update_order(
        self,
        usa_state=None,
        order_number=None,
        home_office_code=None,
        order_status_id=None,
        order_status=None,
    ):
        self.order_number = order_number or self.order_number
        self.usa_state = usa_state or self.usa_state
        self.home_office_code = home_office_code or self.home_office_code
        if order_status_id:
            self.order_status_id = order_status_id
        else:
            self.order_status = order_status
