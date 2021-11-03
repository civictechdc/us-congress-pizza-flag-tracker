from config import flask_app

from OrderController import (
    get_order_by_order_number,
    send_file_qrcode,
    create_order,
    get_orders,
    index,
    get_order_by_uuid,
    update_order,
)

from WebController import info
import UserController
import AuthController
import OfficeController
import StatusController


# TODO: refactor out this from routes:
from flask import Flask, request

# add routes below
flask_app.add_url_rule("/api", view_func=index)
flask_app.add_url_rule("/api/qrcode/<uuid>", view_func=send_file_qrcode, methods=["GET"])

flask_app.add_url_rule("/api/qrcode/<uuid>", view_func=send_file_qrcode, methods=["GET"])

# initialize congress order ID as a UUID.
flask_app.add_url_rule("/api/orders/create", view_func=create_order, methods=["POST"])
# list all the orders
flask_app.add_url_rule("/api/orders", view_func=get_orders, methods=["GET"])
# get specific order
flask_app.add_url_rule("/api/orders/<uuid>", view_func=get_order_by_uuid, methods=["GET"])

flask_app.add_url_rule(
    "/api/order_num/<order_number>",
    view_func=get_order_by_order_number,
    methods=["GET"],
)

flask_app.add_url_rule("/api/info", view_func=info, methods=["GET"])

flask_app.add_url_rule("/api/orders/<uuid>", view_func=update_order, methods=["PUT"])

flask_app.add_url_rule(
    "/api/states", view_func=OfficeController.get_all_states, methods=["GET"]
)

flask_app.add_url_rule(
    "/api/state_offices/<state>",
    view_func=OfficeController.get_offices_by_state,
    methods=["GET"],
)

flask_app.add_url_rule(
    "/api/statuses",
    view_func=StatusController.get_statuses,
    methods=["GET"],
)
