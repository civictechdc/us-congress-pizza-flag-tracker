import json

from flask import render_template, request, send_file, jsonify
import flask

import UserActions
from authorize import token_required, get_exception_if_no_create_update_delete_orders
from config import app, qrcode
import qrcode

# from './http-common.js' import baseURL

from OrderActions import OrderActions
import io


# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode
# from models import UserModel
# from util import table_record_to_json


def index():
    return render_template("index.html")


def create_order():
    request_json = request.get_json()
    usa_state = request_json["usa_state"]
    idbased_order_number = request_json["order_number"]
    office_code = request_json["office_code"]
    order = OrderActions.create(usa_state, idbased_order_number, office_code)
    return f"Created one"


@token_required
def get_orders():
    error_msg = get_exception_if_no_create_update_delete_orders()
    if error_msg:
        return {"message": error_msg}
    orders = OrderActions.get()
    return orders


def get_order_by_uuid(uuid):
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_uuid(uuid)
    order_dict = {}
    order_dict["order_number"] = order_obj.order_number
    order_dict["usa_state"] = order_obj.usa_state
    order_dict["office_code"] = order_obj.office_code
    order_dict["uuid"] = order_obj.uuid
    return order_dict


def get_order_by_order_number(order_number):
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_order_number(order_number)
    if order_obj is None:
        return {"error": "order not found"}
    else:
        order_dict = {}
        order_dict["order_number"] = order_obj.order_number
        order_dict["usa_state"] = order_obj.usa_state
        order_dict["office_code"] = order_obj.office_code
        order_dict["uuid"] = order_obj.uuid
        return {"orders": [order_dict]}


# generate qr code


def get_qrcode(uuid):
    frontendURL = app.config["FRONTEND_URI"]
    img = qrcode.make(frontendURL + "/orders/" + uuid)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return buf


def send_file_qrcode(uuid):
    q = get_qrcode(uuid)
    return send_file(q, mimetype="image/jpeg")


def info():
    headers = flask.request.headers
    return "Request headers:\n" + str(headers)


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


@app.route("/signup", methods=["POST"])
def create_user():
    request_json = request.get_json()
    username = request_json["username"]
    password = request_json["password"]
    can_create_update_delete_orders = request_json["can_create_update_delete_orders"]
    can_update_password_for = request_json["can_update_password_for"]
    can_update_status_for = request_json["can_update_status_for"]
    is_admin = request_json["is_admin"]
    new_user = UserActions.create(
        username,
        password,
        can_create_update_delete_orders,
        can_update_password_for,
        can_update_status_for,
        is_admin,
    )
    return jsonify({"message": "registered successfully"})


@app.route("/signin", methods=["POST"])
def login_user():
    response = UserActions.login_user()
    return response
