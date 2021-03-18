from flask import render_template, redirect, request, session, send_file
from config import db
from models import *
import random

from flask_qrcode import QRcode
from OrderActions import OrderActions 


# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode

def index():
    return render_template('index.html')

def create():
    idbased_order_number = request.form['order_number']
    order = OrderActions.create( "MD",  idbased_order_number , "MD06")
    return f'Created one'

#generate qr code 
def get_qrcode():
    qrcode = QRcode(app)
    data= "team-work"
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")