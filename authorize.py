from flask import jsonify, request
# from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import app
from models import UserModel
import jwt

global_current_user: UserModel = {}

def get_exception_if_no_create_update_delete_orders():
    if (global_current_user.can_create_update_delete_orders != "Y"):
        return "You don't have privileges"
    return None

def get_current_user():
    return global_current_user
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "a valid token is missing"})
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            global global_current_user
            global_current_user = UserModel.query.filter_by(username=data["public_id"]).first()
        except:
            return jsonify({"message": "token is invalid "+token})

        return f(*args, **kwargs)

    return decorator
