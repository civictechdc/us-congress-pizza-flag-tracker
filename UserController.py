from flask import request

from UserActions import UserActions
from config import flask_app
from models import UserParams


@flask_app.route("/api/users/create", methods=["POST"])
def create_user():
    request_json = request.get_json()
    userParams = UserParams()
    userParams.username = request_json["username"]
    userParams.password = request_json["password"]
    userParams.can_create_update_delete_orders = request_json[
        "can_create_update_delete_orders"
    ]
    userParams.can_update_password_for = request_json["can_update_password_for"]
    userParams.can_update_status_for = request_json["can_update_status_for"]
    userParams.is_admin = request_json["is_admin"]
    new_user = UserActions.create(userParams)
    return new_user, 201
