import jwt
from flask import request, make_response

from AuthActions import AuthActions
from config import flask_app
from models import UserModel
global_current_user: UserModel = {}


@flask_app.route("/api/signin", methods=["POST"])
def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(
            "could not verify", 401, {"Authentication": "login required"}
        )
    return AuthActions.login_user(auth.username, auth.password)



def set_authorize_current_user():
    token = None
    if "x-access-tokens" in request.headers:
        token = request.headers["x-access-tokens"]

    if not token:
        raise RuntimeError("A valid token is missing")
    try:
        data = jwt.decode(token, flask_app.config["SECRET_KEY"], algorithms=["HS256"])
        global global_current_user
        global_current_user = UserModel.query.filter_by(
            username=data["public_id"]
        ).first()
    except:
        raise RuntimeError("Invalid user in token")


def get_exception_if_no_create_update_delete_orders():
    if global_current_user.can_create_update_delete_orders != "Y":
        e = Exception()
        e.message = "You do not have the privileges"
        e.status_code = 401
        return e
    return None


def get_current_user():
    return global_current_user