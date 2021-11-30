#/bin/sh
./refresh_db_upgrade.sh
DEBUG=True FLASK_APP=app.py flask db migrate
./refresh_db_upgrade.sh
