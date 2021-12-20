echo 'init script' # runs during prebuild
echo Script will execute the following scripts:

export PIP_USER=false
export PATH=$PATH:$PWD/setup
cp .env.example.mysql .env
create_python_env.sh
source ./activate_python_env.sh
pip_install.sh
db_schema.sh
populate_seed_data.sh
