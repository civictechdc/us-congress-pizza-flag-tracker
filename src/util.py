import datetime
import sys

from flask import jsonify


def get_dict_keyvalue_or_default(dict, key_value, default):
    if key_value in dict:
        return dict[key_value]
    return default


def get_http_response(error_message: str, status: int):
    return jsonify(error_message), status
    # return make_response(error_message, status)


def is_primitive(thing):
    primitive = (int, str, bool, datetime.datetime)
    return isinstance(thing, primitive) or not thing

def is_legit_column(record, column_name):
    value = getattr(record, column_name)
    if column_name.startswith('_'):
        return False
    if is_primitive(value):
        return True

    dict = type(value).__dict__

    if "append" in dict:
        return False
    return True

def make_json_value(record, column_name):
    value = getattr(record, column_name)
    if not value:
        return ""
    if not is_primitive(value):
        if column_name == "time":
            raise BaseException

        return table_record_to_json(value)
    return str(value)

def populate_object_from_json(object, json):
    for key in json:
        setattr(object, key, json[key])
    return object


# Good for debugging
def print_to_debug_log(message):
    original_stdout = sys.stdout
    with open('debug.log', 'a+') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print(datetime.datetime.now(), message)
        sys.stdout = original_stdout

def table_record_to_json(record):
    modelClass = type(record)
    column_names = [column_name for column_name in modelClass.__dict__ if(is_legit_column(record, column_name))]
    json_value = {column_name: make_json_value(record, column_name) for
                  column_name in column_names}
    return json_value


def table_to_json(table):
    return [table_record_to_json(record) for record in table]
