#/bin/sh
echo Upgrading db...
# bring existing db up to date or create new db
DEBUG=True FLASK_APP=app.py flask db upgrade
# create script for any schema changes
DEBUG=True FLASK_APP=app.py flask db migrate
# apply those changes to the db
DEBUG=True FLASK_APP=app.py flask db upgrade
echo Done
