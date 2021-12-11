#/bin/sh
./init_python.sh
# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, python will be activated"|| exit

./refresh_python.sh
# ./check_continue.sh returns false if uses exit to exit

./check_continue.sh "If you enter Y, pip install, db upgrade, and db populate will be run" || exit
./refresh.sh
