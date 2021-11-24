#/bin/sh
./refresh_pip_install.sh
# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, db will be upgraded if necessary"|| exit

./refresh_db_upgrade.sh
# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, data will be populated if necessary" || exit

./populate_seed_data.sh
# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, server will be started"|| exit

./run.sh