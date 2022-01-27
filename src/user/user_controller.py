from flask import request
from src.auth import auth_controller

from src.auth.auth_controller import get_current_user, set_authorize_current_user 
from src.auth.auth_privileges import check_is_admin
from src.user.user_actions import UserActions
from src.user.user_model import UserParams
from src.util import table_record_to_json


def create_user():
    set_authorize_current_user()
    check_is_admin()
    request_json = request.get_json()

    userParams = UserParams()
    userParams.username = request_json["username"]
    userParams.password = request_json["password"]
    userParams.can_create_update_delete_orders = request_json["can_create_update_delete_orders"]
    userParams.office_code = request_json["office_code"]
    userParams.can_update_password_for = request_json["can_update_password_for"]
    userParams.can_update_status_for = request_json["can_update_status_for"]
    userParams.is_admin = request_json["is_admin"]
    new_user = UserActions.create(userParams)
    return table_record_to_json(new_user), 201

def get_current_office():
    current_office = get_current_user().office_code
    if 'FED' == current_office[:3]:
        return 'FED'
    else:
        return current_office

#function for user to update password
def self_update_password(new_password, old_password):
    username = auth_controller.get_current_user().username
    UserActions.self_update_password(username, new_password, old_password)
    return username

def admin_update_password(username, new_password):
    UserActions.admin_update_password(username, new_password)
    return 
