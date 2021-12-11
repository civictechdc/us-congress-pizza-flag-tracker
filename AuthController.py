import datetime
import os
import sys

import jwt
from flask import request, jsonify
from werkzeug.exceptions import BadRequest, Unauthorized

from AuthActions import AuthActions
from config import flask_app
from models import UserModel
from util import get_http_response, table_record_to_json

__current_user__: UserModel = {}


def derive_token_from_username(username):
    days = float(os.environ["TOKEN_EXPIRE_DAYS"])
    token = jwt.encode(
        {
            "public_id": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=days),
        },
        flask_app.config["SECRET_KEY"],
        "HS256",
    )
    return token


def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return get_http_response("Username or password missing.", 401)
    ret_val = table_record_to_json(AuthActions.fetch_user(auth.username, auth.password))
    token = derive_token_from_username(auth.username)
    ret_val["accessToken"] = token
    return ret_val


def set_authorize_current_user():
    global __current_user__

    token = get_token_from_request()
    check_valid_token(token)
    token_username = get_token_username(token)
    __current_user__ = get_user(token_username)


def get_token_from_request():
    token = None
    if "x-access-tokens" in request.headers:
        token = request.headers["x-access-tokens"]
    if not token:
        raise Unauthorized(
            "Credential issue ""Token is missing"", try logging in again.")
    return token


def get_user(token_username):
    try:
        return UserModel.query.filter_by(username=token_username).first()
    except Exception as exception:
        raise Unauthorized(
            f'Invalid username {token_username} in token. Message: "{str(exception)}".  Try logging in again')

def check_valid_token(token):
    try:
        token_data = jwt.decode(token, flask_app.config["SECRET_KEY"], algorithms=["HS256"])
        token_exp_date = datetime.datetime.utcfromtimestamp(token_data["exp"])
        token_expire_days = float(os.environ["TOKEN_EXPIRE_DAYS"])
        token_refresh_after_days = float(os.environ["TOKEN_REFRESH_AFTER_DAYS"])
        refresh_before_exp_date_days = token_expire_days - token_refresh_after_days
        token_refresh_date = token_exp_date - datetime.timedelta(days=refresh_before_exp_date_days)
        if (token_refresh_date < datetime.datetime.utcnow()):
            token_username = token_data["public_id"]
            token = derive_token_from_username(token_username)
            raise Unauthorized("Token is past renew date.  See token in response.", {"refreshedToken": token})
    except Unauthorized as exception:
        raise exception
    except Exception as exception:
        raise Unauthorized(f'Credential issue: {str(exception)}.  Try logging in again.')






def get_token_username(token):
    try:
        token_data = jwt.decode(
            token, flask_app.config["SECRET_KEY"], algorithms=["HS256"])
        token_username = token_data["public_id"]
        return token_username
    except Exception as exception:
        raise Unauthorized(
            f'Credential issue: {str(exception)}.  Try logging in again.')


def get_current_user():
    return __current_user__
