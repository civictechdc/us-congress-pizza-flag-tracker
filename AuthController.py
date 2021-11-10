import jwt
from flask import request
from werkzeug.exceptions import BadRequest

from AuthActions import AuthActions
from config import flask_app
from models import UserModel
from util import get_http_response

__current_user__: UserModel = {}


def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return get_http_response("Username or password missing.", 401)
    ret_val["accessToken"] = get_token_with_username(user.username)
    return ret_val

    return AuthActions.login_user(auth.username, auth.password)


def set_authorize_current_user():
    global __current_user__

    token = get_token_from_request()
    token_username = get_token_username(token)
    __current_user__ = get_user(token_username)


def get_token_from_request():
    token = None
    if "x-access-tokens" in request.headers:
        token = request.headers["x-access-tokens"]
    if not token:
        raise BadRequest(
            "Credential issue ""Token is missing"", try logging in again.")
    return token


def get_user(token_username):
    try:
        return UserModel.query.filter_by(username=token_username).first()
    except Exception as exception:
        raise BadRequest(
            f'Invalid username {token_username} in token. Message: "{str(exception)}".  Try logging in again')


def get_token_username(token):
    try:
        token_data = jwt.decode(
            token, flask_app.config["SECRET_KEY"], algorithms=["HS256"])
        token_username = token_data["public_id"]
    except Exception as exception:
        raise BadRequest(
            f'Credential issue: {str(exception)}.  Try logging in again.')
    return token_username


def get_current_user():
    return __current_user__
