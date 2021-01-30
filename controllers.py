from flask import render_template, redirect, request, session
from config import db
from models import *

# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode

def index():
    return render_template('index.html')