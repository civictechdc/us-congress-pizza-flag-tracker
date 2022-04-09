from config import flask_app, db
from src import routes
from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

from src.order.order_actions import OrderActions
from src.util import table_to_json


if __name__ == "__main__":
    flask_app.run(debug=True)

