import json


def get_office_codes_list():
    with open(
        "data/office_codes.json",
    ) as office_codes_json:
        office_codes_list = json.load(office_codes_json)
    return office_codes_list
