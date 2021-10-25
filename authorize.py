from flask import jsonify, request

# from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import app
from models import UserModel
import jwt

global_current_user: UserModel = {}


def get_exception_if_no_create_update_delete_orders():
    if global_current_user.can_create_update_delete_orders != "Y":
        e = Exception()
        e.message = "You do not have the privileges"
        e.status_code = 401
        return e
    return None


def get_current_user():
    return global_current_user

