echo 'init script' # runs during prebuild
export PIP_USER=false
cp .env.example.mysql .env
./init_python.sh
./refresh_python.sh
./refresh_pip_install.sh
./refresh_db_upgrade.sh
./populate_seed_data.sh

