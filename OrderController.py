from flask import render_template, request, send_file

from authorize import token_required, get_exception_if_no_create_update_delete_orders
from config import app, qrcode
import qrcode

# from './http-common.js' import baseURL

from OrderActions import OrderActions
import io


# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode
from models import UserParams
from util import table_record_to_json

# @app.route("/users/create", methods=["POST"])
# def create_user():
#     request_json = request.get_json()
#     userParams = UserParams()
#     userParams.username = request_json["username"]
#     userParams.password = request_json["password"]
#     userParams.can_create_update_delete_orders = request_json["can_create_update_delete_orders"]
#     userParams.can_update_password_for = request_json["can_update_password_for"]
#     userParams.can_update_status_for = request_json["can_update_status_for"]
#     userParams.is_admin = request_json["is_admin"]
#     new_user = UserActions.create(userParams)
#     return new_user;

def index():
    return render_template("index.html")

@token_required
def create_order():
    e = get_exception_if_no_create_update_delete_orders()
    if (e):
        return {"message": e.message}, e.status_code
    request_json = request.get_json()
    usa_state = request_json["usa_state"]
    idbased_order_number = request_json["order_number"]
    office_code = request_json["office_code"]
    order = OrderActions.create(usa_state, idbased_order_number, office_code)
    return table_record_to_json(order)


@token_required
def get_orders():
    orders = OrderActions.get()
    return orders


@token_required
def get_order_by_uuid(uuid):
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_uuid(uuid)
    order_dict = {}
    order_dict["order_number"] = order_obj.order_number
    order_dict["usa_state"] = order_obj.usa_state
    order_dict["office_code"] = order_obj.office_code
    order_dict["uuid"] = order_obj.uuid
    return order_dict


@token_required
def get_order_by_order_number(order_number):
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_order_number(order_number)
    order_dict = {}
    order_dict["order_number"] = order_obj.order_number
    order_dict["usa_state"] = order_obj.usa_state
    order_dict["office_code"] = order_obj.office_code
    order_dict["uuid"] = order_obj.uuid
    return {"orders": [order_dict]}


@token_required
def get_qrcode(uuid):
    frontendURL = app.config["FRONTEND_URI"]
    img = qrcode.make(frontendURL + "/orders/" + uuid)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return buf

@token_required
def send_file_qrcode(uuid):
    q = get_qrcode(uuid)
    return send_file(q, mimetype="image/jpeg")

@token_required
def update_order(uuid):
    request_json = request.get_json()
    usa_state = request_json["usa_state"]
    idbased_order_number = request_json["order_number"]
    office_code = request_json["office_code"]
    updated_order = OrderActions.update_order(
        uuid, usa_state, idbased_order_number, office_code
    )
    order_dict = {}
    order_dict["order_number"] = updated_order.order_number
    order_dict["usa_state"] = updated_order.usa_state
    order_dict["office_code"] = updated_order.office_code
    order_dict["uuid"] = updated_order.uuid
    return order_dict

