from flask import render_template, redirect, request, session, send_file
import flask
from config import app, db, qrcode
from models import OrderModel
import cv2
import qrcode
#from './http-common.js' import baseURL


import random
import json

from OrderActions import OrderActions 
import io


# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode

def index():
    return render_template('index.html')

def create_order():
    request_json = request.get_json()
    print(request_json, type(request_json))
    # for x in request_json.keys():
    #     print(x,request_json[x])

    usa_state = request_json[u'usa_state']
    idbased_order_number = request_json[u'order_number']
    coffice = request_json[u'coffice']
    order = OrderActions.create( usa_state,  idbased_order_number , coffice)
    return f'Created one'

def get_orders():
    orders=OrderActions.get()
    return orders

def get_order_by_uuid(uuid):
    # Return a dictionary(json) object for use by frontend
    order_obj = OrderActions.get_order_by_uuid(uuid)
    order_dict = {}
    order_dict['order_number'] = order_obj.order_number
    order_dict['usa_state'] = order_obj.usa_state
    order_dict['coffice'] = order_obj.coffice
    order_dict['uuid'] = order_obj.uuid
    return order_dict

#generate qr code 
def get_qrcode(uuid):
    img = qrcode.make('http://localhost:3000/orders/'+uuid)
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
    print(request_json, type(request_json))
    # for x in request_json.keys():
    #     print(x,request_json[x])

    usa_state = request_json[u'usa_state']
    idbased_order_number = request_json[u'order_number']
    coffice = request_json[u'coffice']
    updated_order = OrderActions.update_order( uuid, usa_state, idbased_order_number , coffice)
    return updated_order