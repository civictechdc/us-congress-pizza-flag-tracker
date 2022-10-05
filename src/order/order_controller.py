import keyword
import os
from flask import render_template, request, send_file, Response
from data.scripts.add_stable_orders import add_stable_orders
from werkzeug.exceptions import Unauthorized
from data.scripts.data_util import get_office_codes_list
from src.order_log import order_log_controller
from src.util import table_record_to_json, get_dict_keyvalue_or_default
from config import flask_app, qrcode, db
import qrcode
from src.auth import auth_controller, auth_privileges
from src.order.order_actions import OrderActions, OrderQueryParams
import io


def index():
    return render_template("index.html")


def create_order():
    auth_controller.set_authorize_current_user()
    auth_privileges.check_update_order_allowed()
    request_json = request.get_json()
    usa_state = request_json["usa_state"]
    idbased_order_number = request_json["order_number"]
    home_office_code = request_json["home_office_code"]
    order_status_id = get_dict_keyvalue_or_default(request_json, "order_status_id", 1)
    order = OrderActions.create(
        usa_state, idbased_order_number, home_office_code, order_status_id
    )
    return table_record_to_json(order)


def get_orders():

    auth_controller.set_authorize_current_user()
    restrict_office = auth_privileges.get_current_office()
    if restrict_office[:3] == "FED":
        restrict_office = None
    usa_state = request.args.get("state")
    statuses = request.args.get("status")
    office_code = restrict_office or request.args.get("office")
    keyword = request.args.get("keyword")
    order_number = request.args.get("order_number")
    query_params = OrderQueryParams()
    if usa_state:
        query_params.usa_state = usa_state
    if statuses:
        query_params.statuses = statuses
    if office_code:
        query_params.office_code = office_code
    if keyword:
        query_params.keyword = keyword
    if order_number:
        query_params.order_number = order_number

    orders = OrderActions.get_orders(query_params)
    orders_json = [table_record_to_json(order) for order in orders]
    replace_mock_state_placeholders(orders_json)
    return {"orders": orders_json}
    # [table_record_to_json(order) for order in orders]}


def get_order_by_uuid(uuid):
    auth_controller.set_authorize_current_user()
    order_obj = OrderActions.get_order_by_uuid(uuid)
    order_dict = table_record_to_json(order_obj)
    replace_mock_state_placeholder(order_dict)
    return order_dict


def delete_order_by_uuid(uuid):
    auth_controller.set_authorize_current_user()
    order_obj = OrderActions.get_order_by_uuid(uuid)
    if order_obj is None:
        return Response(response="Error:order not found", status=404)
    else:
        OrderActions.delete_order_by_uuid(uuid)
        return "Deleted", 204


def get_order_by_order_number(order_number):
    auth_controller.set_authorize_current_user()
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_order_number(order_number)
    if order_obj is None:
        return {"error": "order not found"}
    else:
        order_dict = table_record_to_json(order_obj)
        replace_mock_state_placeholder(order_dict)
        return {"orders": [order_dict]}


# generate qr code - qr code points to Scan view on frontend
def get_qrcode(uuid):
    frontend_url = flask_app.config["FRONTEND_URI"]

    # remember this is the frontend URL, so no need for /api/ prefix
    img = qrcode.make(frontend_url + "/scan/" + uuid)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return buf


# not secured as it is provided in a link where token cannot be sent
def send_file_qrcode(uuid):
    q = get_qrcode(uuid)
    return send_file(q, mimetype="image/jpeg")


def update_order(uuid):
    auth_controller.set_authorize_current_user()
    order: OrderActions = OrderActions.get_order_by_uuid(uuid)
    auth_privileges.check_update_order_allowed()

    request_json = request.get_json()
    usa_state = get_dict_keyvalue_or_default(request_json, "usa_state", None)
    home_office_code = get_dict_keyvalue_or_default(
        request_json, "home_office_code", None
    )
    order_number = get_dict_keyvalue_or_default(request_json, "order_number", None)
    order_status_id = get_dict_keyvalue_or_default(
        request_json, "order_status_id", None
    )
    archived = get_dict_keyvalue_or_default(request_json, "archived", None)
    order = OrderActions.update_order_by_uuid(
        uuid, usa_state, order_number, home_office_code, order_status_id, archived
    )
    order_dict = table_record_to_json(order)
    return order_dict


def update_order_status(uuid):
    auth_controller.set_authorize_current_user()

    request_json = request.get_json()
    new_order_status_id = get_dict_keyvalue_or_default(
        request_json, "order_status_id", None
    )
    order: OrderActions = OrderActions.get_order_by_uuid(uuid)
    auth_privileges.check_update_status_allowed(order)

    order = OrderActions.update_order_by_uuid(
        uuid=uuid, order_status_id=new_order_status_id
    )
    order_dict = table_record_to_json(order)
    return order_dict


# check to see if this query is handled in get_orders
def get_orders_by_office():
    auth_controller.set_authorize_current_user()
    current_office = auth_privileges.get_current_office()
    offices = OrderActions.get_orders(current_office)
    office_json = [table_record_to_json(office) for office in offices]
    return {"orders": office_json}


def get_orders_by_usa_state():
    auth_controller.set_authorize_current_user()
    current_office = auth_privileges.get_current_office()
    states = OrderActions.get_orders_by_usa_state(current_office)
    state_json = [table_record_to_json(state) for state in states]
    return {"orders": state_json}


def get_orders_by_order_status_id(order_status_id):
    auth_controller.set_authorize_current_user()
    statuses = OrderActions.get_orders_by_order_status_id(order_status_id)
    status_jason = [table_record_to_json(status) for status in statuses]
    return {"orders": status_jason}


def replace_mock_state_placeholders(orders_json):
    for order in orders_json:
        replace_mock_state_placeholder(order)


def replace_mock_state_placeholder(order):
    if not (order["person"] and order["person"]["town"]):
        return
    person_constituent_town = order["person"]["town"]
    usa_state = order["usa_state"]
    new_constituent_town = person_constituent_town.replace("<state>", usa_state)
    order["person"]["town"] = new_constituent_town


def reset():
    flask_env = os.environ["FLASK_ENV"]
    if not (flask_env == "development" or flask_env == "test"):
        raise Unauthorized("reset not allowed for FLASK_ENV " + flask_env)
    office_codes_list = get_office_codes_list()
    add_stable_orders(office_codes_list=office_codes_list, db=db)
    return {"reset": "success"}
