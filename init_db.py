from typing import NamedTuple
import click
from flask.cli import with_appcontext
from flask import current_app, g
from config import db, flask_app
import json

from initial_data.init_office_table import init_office_table
from initial_data.init_user_table import (
    init_user_table_state_users,
    init_user_table_fed_users,
)
from initial_data.init_status_table import init_status_table
from initial_data.init_orders_table import init_orders_table


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    # imports are inside, otherwise we get circular import during testing
    with open(
        "./initial_data/office_codes.json",
    ) as office_codes_json:
        office_codes_list = json.load(office_codes_json)

    with open("./initial_data/users.json") as users_json:
        users_list = json.load(users_json)

    with open("./initial_data/statuses.json") as statuses_json:
        statuses_list = json.load(statuses_json)

    # add FED and state offices to office table
    init_office_table(office_codes_list, db)
    # add state office users to user table
    init_user_table_state_users(office_codes_list, db)
    # add fed office users to user table
    init_user_table_fed_users(users_list, db)
    # add flag statuses to status table
    init_status_table(statuses_list, db)
    # initialize orders table with fake orders if in dev mode
    print("DB is in debug mode: " + str(flask_app.debug))
    print("DB is in mode: " + str(flask_app.env))
    if flask_app.env == "development":

        init_orders_table(office_codes_list, db)

    db.session.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
