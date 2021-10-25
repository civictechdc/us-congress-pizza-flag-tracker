from flask import render_template, request, send_file
from util import table_record_to_json
from authorize import get_exception_if_no_create_update_delete_orders
from config import app, qrcode
import qrcode
from AuthController import set_authorize_current_user
# from './http-common.js' import baseURL

from OrderActions import OrderActions
import io


def index():
    return render_template("index.html")


def create_order():
    set_authorize_current_user()
    e = get_exception_if_no_create_update_delete_orders()
    if e:
        return {"message": e.message}, e.status_code
    request_json = request.get_json()
    usa_state = request_json["usa_state"]
    idbased_order_number = request_json["order_number"]
    home_office_code = request_json["home_office_code"]
    order_status = 1
    order = OrderActions.create(usa_state, idbased_order_number, home_office_code, order_status)
    return table_record_to_json(order)


def get_orders():
    set_authorize_current_user()
    orders = OrderActions.get()
    return orders


def get_order_by_uuid(uuid):
    # Return a dictionary(json) object for use by frontend
    set_authorize_current_user()
    order_obj = OrderActions.get_order_by_uuid(uuid)
    order_dict = {"order_number": order_obj.order_number, "usa_state": order_obj.usa_state,
                  "home_office_code": order_obj.home_office_code, "uuid": order_obj.uuid}
    return order_dict


def get_order_by_order_number(order_number):
    set_authorize_current_user()
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_order_number(order_number)
    if order_obj is None:
        return {"error": "order not found"}
    else:
        order_dict = {"order_number": order_obj.order_number, "usa_state": order_obj.usa_state,
                      "home_office_code": order_obj.home_office_code, "uuid": order_obj.uuid}
        return {"orders": [order_dict]}


# generate qr code
def get_qrcode(uuid):
    frontend_url = app.config["FRONTEND_URI"]
    img = qrcode.make(frontend_url + "/api/orders/" + uuid)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return buf


# not secured as it is provided in a link where token cannot be sent
def send_file_qrcode(uuid):
    q = get_qrcode(uuid)
    return send_file(q, mimetype="image/jpeg")


def update_order(uuid):
    set_authorize_current_user()
    request_json = request.get_json()
    usa_state = request_json["usa_state"]
    idbased_order_number = request_json["order_number"]
    office_code = request_json["home_office_code"]
    updated_order = OrderActions.update_order(
        uuid, usa_state, idbased_order_number, office_code
    )
    order_dict = {"order_number": updated_order.order_number, "usa_state": updated_order.usa_state,
                  "home_office_code": updated_order.office_code, "uuid": updated_order.uuid}
    return order_dict
