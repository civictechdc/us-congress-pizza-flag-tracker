#!/bin/sh
rm -rf migrations
rm flag*.db
DEBUG=True FLASK_APP=app.py flask db init
DEBUG=True FLASK_APP=app.py flask db migrate
DEBUG=True FLASK_APP=app.py flask db upgrade
#DEBUG=True FLASK_APP=app.py flask init-db
cp flag.db flagtests.db
