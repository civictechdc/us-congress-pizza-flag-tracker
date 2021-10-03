from config import app
from controllers import get_order_by_order_number, info, send_file_qrcode, create_order, get_orders, index, get_order_by_uuid, update_order, get_all_states, get_offices_by_state

# TODO: refactor out this from routes:
from flask import Flask, render_template, request, send_file

# add routes below
app.add_url_rule('/', view_func=index)
# create qr code
#app.add_url_rule('/createqrcode/<orderid>', view_func=send_file_qrcode, methods=["GET"])

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

app.add_url_rule('/api/states',view_func=get_all_states,methods = ["GET"])

app.add_url_rule('/api/state_offices/<state>',view_func=get_offices_by_state,methods=["GET"])