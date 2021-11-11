import json

from config import db
from models import UserModel


def table_record_to_json(record):
    modelClass = type(record)
    columns = [record for record in filter(lambda item: not item.startswith('_'),modelClass.__dict__)]
    json_value = {column_name: str(getattr(record, column_name))for column_name in columns}
    return json_value



def table_to_json(table):
    return { "data": [table_record_to_json(record) for record in table] }


def dict_keyvalue_or_default (dict, key_value, default):
    if key_value in dict:
        return dict[key_value]
    return default