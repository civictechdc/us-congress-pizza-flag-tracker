from config import app, db
import routes
from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


if __name__ == "__main__":
    app.run(debug=True)
