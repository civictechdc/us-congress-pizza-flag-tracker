#/bin/sh
pip install -r requirements.txt
DEBUG=True FLASK_APP=app.py flask db upgrade
./populate_seed_data.sh
echo If you enter Y, server will be started
./check_continue.sh || exit
./run.sh


