from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_cors import CORS
from flask_qrcode import QRcode
import os
import qrcode

flask_app = Flask(__name__)
qrcode = QRcode(flask_app)

CORS(flask_app, resources=r"/api/*")
flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
flask_app.config["FRONTEND_URI"] = os.environ["FRONTEND_URI"]
flask_app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
#squelch warning, per https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(flask_app)

from init_db import init_app

init_app(flask_app)

migrate = Migrate(flask_app, db)
