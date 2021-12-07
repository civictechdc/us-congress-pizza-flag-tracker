echo 'init script' # runs during prebuild
export PIP_USER=false
cp .env.example .env
pip3 install -r requirements.txt
DEBUG=True FLASK_APP=app.py flask db upgrade
python populate_seed_data.py