from typing import NamedTuple
import click 
from flask.cli import with_appcontext
from flask import current_app, g 
from config import db
from models import OfficeModel, StatusModel, UserParams, UserModel
import json
# import uuid

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    with open('./initial_data/office_codes.json',) as office_codes_json:
        office_codes_list = json.load(office_codes_json)
    
    # add state offices to office table
    for state_offices in office_codes_list:
        usa_state = state_offices["usa_state"]
        for office_code in state_offices["office_code"]:
            # TODO(tdk): we may not need uuids, discuss
            # theUuid = str(uuid.uuid4())
            office = OfficeModel(usa_state, office_code)
            db.session.add(office)

    # add state office users to user table
    for state_offices in office_codes_list[1:]:
        usa_state = state_offices["usa_state"]
        for office_code in state_offices["office_code"]:
            # Normal users
            params = UserParams()
            params.username = office_code
            params.password = office_code + "-1010"
            params.office_code = office_code
            params.can_create_update_delete_orders = "N"
            params.can_update_status_for = "office_code"
            params.can_update_password_for = "NONE"
            params.is_admin = "N"
            user = UserModel(params)
            db.session.add(user)
            # Admin users
            params.username = office_code + "-ADMIN"
            params.password = office_code + "-ADMIN-1010"
            params.office_code = office_code
            params.can_update_password_for = office_code
            user = UserModel(params)
            db.session.add(user)

    with open('./initial_data/users.json') as users_json:
        users_list = json.load(users_json)

    for user in users_list:
        params = UserParams()
        params.username = user["username"]
        params.password = user["password"]
        params.office_code = user["office_code"]
        params.can_create_update_delete_orders = user["can_create_update_delete_orders"]
        params.can_update_status_for = user["can_update_status_for"]
        params.can_update_password_for = user["can_update_password_for"]
        params.is_admin = user["is_admin"]

        user_ = UserModel(params)
        db.session.add(user_)

    with open('./initial_data/statuses.json') as statuses_json:
        statuses_list = json.load(statuses_json)

    for status in statuses_list:
        id = status["id"]
        status_federal_office_code = status["status_federal_office_code"]
        sequence_num = status["sequence_num"]
        description = status["description"]
        status = StatusModel(id,status_federal_office_code,sequence_num,description)
        db.session.add(status)

    db.session.commit()
 
    

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)