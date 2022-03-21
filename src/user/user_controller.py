from flask import request, Response
from src.auth import auth_controller, auth_privileges

from src.user.user_actions import UserActions
from src.user.user_model import UserParams
from src.util import populate_object_from_json, table_record_to_json

def create_user():
    auth_controller.set_authorize_current_user()
    auth_privileges.check_is_admin()
    request_json = request.get_json()
    userParams = UserParams()
    populate_object_from_json(userParams, request_json)

    new_user = UserActions.create(userParams)
    retval = table_record_to_json(new_user)
    return retval, 201

def get_all_users():
    auth_privileges.check_is_admin()
    all_users = UserActions.get_users()
    return table_record_to_json(all_users), 201
    
def get_current_office():
    current_office = auth_privileges.get_current_user().office_code
    if "FED" == current_office[:3]:
        return "FED"
    else:
        return current_office


# function for user to update password
# function needs to be refactored
def self_update_password():
    request_json = request.get_json()["data"]
    old_password = request_json["old_password"]
    new_password = request_json["new_password"]

    username = auth_privileges.get_current_user().username

    if UserActions.self_update_password(username, new_password, old_password):
        return Response(response=username, status=200)
    else:
        return
        # this will NOT tell the user if their old password is incorrect--we need to add some additional error handling that will send responses back from the server, not just raise an exception.
        # See https://flask.palletsprojects.com/en/2.0.x/errorhandling/ for one approach using decorators to catch exceptions


def admin_update_password(username, new_password):
    UserActions.admin_update_password(username, new_password)
    return
