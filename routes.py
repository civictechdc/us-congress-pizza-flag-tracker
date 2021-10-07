from config import app
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

# TODO: refactor out this from routes:
from flask import Flask, render_template, request, send_file

# add routes below
app.add_url_rule("/api", view_func=index)
app.add_url_rule("/api/qrcode/<uuid>", view_func=send_file_qrcode, methods=["GET"])

app.add_url_rule('/api/qrcode/<uuid>',
                 view_func=send_file_qrcode, methods=["GET"])

# initialize congress order ID as a UUID.
app.add_url_rule('/api/orders/create',
                 view_func=create_order, methods=["POST"])
# list all the orders
app.add_url_rule('/api/orders', view_func=get_orders, methods=["GET"])
# get specific order
app.add_url_rule('/api/orders/<uuid>',
                 view_func=get_order_by_uuid, methods=["GET"])

app.add_url_rule('/api/order_num/<order_number>',
                 view_func=get_order_by_order_number, methods=["GET"])

app.add_url_rule('/api/info', view_func=info, methods=["GET"])

app.add_url_rule('/api/orders/<uuid>', view_func=update_order, methods=["PUT"])
