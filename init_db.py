import click
from flask.cli import with_appcontext
from flask import g
from config import db
import json




def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
