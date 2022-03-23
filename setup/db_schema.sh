#/bin/sh
echo Upgrading db...
# bring existing db up to date or create new db
DEBUG=True FLASK_APP=app.py flask db upgrade
# create additional migration scripts if there are any changes to schema
DEBUG=True FLASK_APP=app.py flask db migrate
# run upgrade again to apply any schema changes from previous step to the current db
DEBUG=True FLASK_APP=app.py flask db upgrade
echo Done
