from flask import render_template, request, send_file

from StatusActions import StatusActions

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e5b60bac93655058362969d53e983eb182261f50
from util import table_record_to_json, get_dict_keyvalue_or_default
from config import flask_app, qrcode
import AuthController
from util import print_to_debug_log

<<<<<<< HEAD
def get_statuses():
    AuthController.set_authorize_current_user()
    statuses = StatusActions.get_statuses()
    return {"statuses": [table_record_to_json(status) for status in statuses]}
=======

def get_statuses():
    return {"statuses": table_to_json(StatusActions.get_statuses())}
>>>>>>> 66fd9f5 (rename order_status to order_status_id)
=======
def get_statuses():
    AuthController.set_authorize_current_user()
    statuses = StatusActions.get_statuses()
    return {"statuses": [table_record_to_json(status) for status in statuses]}
>>>>>>> e5b60bac93655058362969d53e983eb182261f50
