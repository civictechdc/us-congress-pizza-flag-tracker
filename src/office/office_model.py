from config import db
from pickle import NONE
from sqlalchemy import func
from sqlalchemy.sql.expression import join

class OfficeModel(db.Model):
    __tablename__ = "offices"
    # TODO(tdk): commenting out uuid as this may not be needed with un/pw login
    # uuid = db.Column(db.String(40), unique=True, index=True, nullable=False)
    office_code = db.Column(db.String(10), primary_key=True, nullable=False)
    usa_state = db.Column(db.String(10))
    users = db.relationship("UserModel")
    orders = db.relationship("OrderModel")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __init__(self, usa_state, office_code):
        # see above about not needing uuid
        # self.uuid = theUuid
        self.office_code = office_code
        self.usa_state = usa_state