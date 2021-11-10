import json
import traceback

from flask import make_response, jsonify
from werkzeug.exceptions import HTTPException

from config import flask_app


def get_dict_keyvalue_or_default(dict, key_value, default):
    if key_value in dict:
        return dict[key_value]
    return default


def get_http_response(error_message: str, status: int):
    return jsonify(error_message), status
    # return make_response(error_message, status)


@flask_app.errorhandler(Exception)
def handle_exceptions_for_app(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    print("Message:",str(e))
    print(traceback.print_exc())
    return jsonify(error=str(e)), code

def table_record_to_json(record):
    modelClass = type(record)
    columns = [record for record in filter(lambda item: not item.startswith('_'), modelClass.__dict__)]
    json_value = {column_name: str(getattr(record, column_name)) for column_name in columns}
    return json_value


def table_to_json(table):
    return {"data": [table_record_to_json(record) for record in table]}


