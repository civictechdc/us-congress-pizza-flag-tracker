import jwt
from flask import request

from AuthActions import AuthActions
from config import app
from models import UserModel


@app.route("/api/signin", methods=["POST"])
def login_user():
    response = AuthActions.login_user()
    return response


def set_authorize_current_user():
    token = None
    if "x-access-tokens" in request.headers:
        token = request.headers["x-access-tokens"]

    if not token:
        raise RuntimeError("A valid token is missing")
    try:
        data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        global global_current_user
        global_current_user = UserModel.query.filter_by(
            username=data["public_id"]
        ).first()
    except:
        raise RuntimeError("Invalid user in token")
