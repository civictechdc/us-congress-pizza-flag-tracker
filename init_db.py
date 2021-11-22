import click
from flask.cli import with_appcontext
from flask import g
from config import db
import json


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()



@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
