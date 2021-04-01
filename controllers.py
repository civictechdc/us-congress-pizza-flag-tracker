from flask import render_template, redirect, request, session, send_file
from config import db
from models import *
import random
import json

from flask_qrcode import QRcode
from OrderActions import OrderActions 


# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode

def index():
    return render_template('index.html')

def create():
    request_json = request.get_json()
    print(request_json, type(request_json))
    # for x in request_json.keys():
    #     print(x,request_json[x])

    usa_state = request_json[u'usa_state']
    idbased_order_number = request_json[u'order_number']
    coffice = request_json[u'coffice']
    order = OrderActions.create( usa_state,  idbased_order_number , coffice)
    return f'Created one'

#generate qr code 
def get_qrcode():
    qrcode = QRcode(app)
    data= "team-work"
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")