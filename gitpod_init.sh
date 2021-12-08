echo 'init script' # runs during prebuild
export PIP_USER=false
cp .env.example .env
echo Setting up myenv
python -m venv myenv
chmod 700 myenv/bin/*
chmod 700 myenv/bin/*.*
echo Activating 
myenv/bin/activate
pip3 install -r requirements.txt
DEBUG=True FLASK_APP=app.py flask db upgrade
python populate_seed_data.py