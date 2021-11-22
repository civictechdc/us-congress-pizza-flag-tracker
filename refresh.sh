#/bin/sh
pip install -r requirements.txt
DEBUG=True FLASK_APP=app.py flask db upgrade


  pause Press any key to start server, Ctrl-C to terminate
#./run.sh


