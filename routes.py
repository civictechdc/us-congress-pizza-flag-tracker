#from config import app
from controllers import *

# TODO: refactor out this from routes:
from flask import Flask, render_template, request, send_file



# add routes below
app.add_url_rule('/', view_func=index)
# create qr code
app.add_url_rule('/qrcode', view_func=get_qrcode, methods=["GET"])
#initialize congress order ID as a UUID.
app.add_url_rule('/create', view_func=create, methods=["POST"])