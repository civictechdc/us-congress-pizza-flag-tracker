from flask import render_template, request, send_file, Response
from src.order_log import order_log_controller
from src.util import table_record_to_json, get_dict_keyvalue_or_default
from config import flask_app, qrcode, db
import qrcode
from src.auth import auth_controller, auth_privileges
from src.order.order_actions import OrderActions
import io

constituents = [
   ["Paul Revere", "32 Battle Road", "Lexington", "02476", "(111) 415-1775"],
   ["Bugs Bunny", "32 Looney Tune Road", "Cwazy Rabbit", "02174", "(WHA) TSU-PDOC"],
   ["Kamala Harris", "1 Whitehouse", "Pleasantville", "41923", "(111) 347-0000"],
   ["Sirius Black", "12 Grimmauld Place", "Magic", "12345", "(123) 321-1234"],
   ["Mrs Addams", "001 Cemetery Lane", "Death Hollow", "34521", "(617) 862-7731"],
   ["Harriet Tubman", "000 Secret Street", "Hiddenville", "00000", ""]
]
order_mock_constituent_dict = {}

# mock person data for proof of concept demo
# in production, person data would come from external system
def add_mock_constituents(orders_dict):
    x = 0
    for order_dict in orders_dict:
        uuid = order_dict["uuid"]
        order_mock_constituent_dict[uuid] = constituents[x]
        add_mock_constituent(order_dict)

        x = x + 1
        if x == len(constituents):
            x = 0

# mock person data for proof of concept demo
# in production, person data would come from external system
def add_mock_constituent(order_dict):
    if len(order_mock_constituent_dict) == 0:
        get_orders() ## populates order_mock_constituent_dict
    mock_constituent = order_mock_constituent_dict[order_dict["uuid"]]
    mock_json = {"name": mock_constituent[0], \
                  "address": mock_constituent[1], \
                  "town": mock_constituent[2] + ", " + order_dict["usa_state"] + " " + mock_constituent[3], \
                  "phone": mock_constituent[4] \
                  }
    order_dict["person"] = mock_json          



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
    current_office = auth_privileges.get_current_office()
    orders = OrderActions.get(current_office)
    orders_json = [table_record_to_json(order) for order in orders]
    add_mock_constituents(orders_json)

    return {"orders": orders_json}
    # [table_record_to_json(order) for order in orders]}




def get_order_by_uuid(uuid):
    auth_controller.set_authorize_current_user()
    order_obj = OrderActions.get_order_by_uuid(uuid)
    order_dict = table_record_to_json(order_obj)
    add_mock_constituent(order_dict)
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
        add_mock_constituent(order_dict)
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
    order = OrderActions.update_order_by_uuid(
        uuid, usa_state, order_number, home_office_code, order_status_id
    )
    order_dict = table_record_to_json(order)
    return order_dict


def update_order_status(uuid):
    auth_controller.set_authorize_current_user()

    request_json = request.get_json()
    new_order_status_id = get_dict_keyvalue_or_default(
        request_json, "order_status_id", None
    )
    auth_privileges.check_update_status_allowed(order)

    order = OrderActions.update_order_by_uuid(uuid=uuid, order_status_id=new_order_status_id)
    order_dict = table_record_to_json(order)
    return order_dict
