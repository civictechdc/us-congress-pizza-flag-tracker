import click 
from flask.cli import with_appcontext
from flask import current_app, g 
from config import db
from models import OfficeModel
import json
# import uuid

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    with open('office_codes.json',) as office_codes_json:
        office_codes_list = json.load(office_codes_json)
    
    for state_offices in office_codes_list:
        usa_state = state_offices["usa_state"]
        for office_code in state_offices["office_code"]:
            # TODO(tdk): we may not need uuids, discuss
            # theUuid = str(uuid.uuid4())
            office = OfficeModel(usa_state, office_code)
            db.session.add(office)
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