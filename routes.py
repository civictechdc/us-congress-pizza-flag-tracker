from config import app
from controllers import *

# TODO: refactor out this from routes:
from flask import Flask, render_template, request, send_file

from flask_qrcode import QRcode
qrcode = QRcode(app)

# add routes below
app.add_url_rule('/', view_func=index)

# TODO: refactor into controller and agree on standard format for controllers
@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = "team-work"
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")