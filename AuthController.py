import jwt
from flask import request, make_response
from werkzeug.exceptions import Unauthorized

from AuthActions import AuthActions
from OrderActions import OrderActions
from config import flask_app
from models import UserModel

__current_user__: UserModel = {}

def check_is_admin():
    if __current_user__.is_admin != "Y":
        raise Unauthorized("Unauthorized.  Admin privileges required.")

def check_update_order_allowed():
    if get_current_user().can_create_update_delete_orders != "Y":
        raise Unauthorized("Unauthorized.  Create/update/delete order privileges required.")


def check_update_status_allowed(order: OrderActions):
    is_update_status_allowed = \
        get_current_user().can_create_update_status_for == "ALL" or \
        get_current_user().can_update_status_for == order.home_office_code
    if not is_update_status_allowed():
        raise Unauthorized("Unauthorized.  Update status privileges must be ALL or " + order.home_office_code)


def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(
            "could not verify", 401, {"Authentication": "login required"}
        )
    return AuthActions.login_user(auth.username, auth.password)


def set_authorize_current_user():
    global __current_user__
    token = None

    if "x-access-tokens" in request.headers:
        token = request.headers["x-access-tokens"]

    if not token:
        raise RuntimeError("A valid token is missing")

    try:
        token_data = jwt.decode(token, flask_app.config["SECRET_KEY"], algorithms=["HS256"])
        token_username = token_data["public_id"]
        if global_user_is_not_set(token_username):
            __current_user__ = UserModel.query.filter_by(username=token_username).first()
    except:
        raise RuntimeError("Invalid username in token")


def global_user_is_not_set(token_username):
    is_logged_in = hasattr(__current_user__, "username")
    return not (is_logged_in and __current_user__ and __current_user__.username == token_username)


def get_current_user():
    return __current_user__
