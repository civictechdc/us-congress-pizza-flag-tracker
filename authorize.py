from flask import jsonify, request

# from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import app
from models import UserModel
import jwt

global_current_user: UserModel = {}


def get_exception_if_no_create_update_delete_orders():
    if global_current_user.can_create_update_delete_orders != "Y":
        print("here", global_current_user.can_create_update_delete_orders)
        e = Exception()
        e.message = "You do not have the privileges"
        e.status_code = 401
        return e
    return None


def get_current_user():
    return global_current_user


def get_current_user():
    return global_current_user


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]

        if not token:
            return {"message": "a valid token is missing"}, 401
        try:
            print("decoding1")
            print("decoding2", app.config["SECRET_KEY"], jsonify(token))
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            print("decoded")
            global global_current_user
            global_current_user = UserModel.query.filter_by(
                username=data["public_id"]
            ).first()
        except:
            print("decoding3")
            return jsonify({"message": "token is invalid "}), 401

        return f(*args, **kwargs)

    return decorator
