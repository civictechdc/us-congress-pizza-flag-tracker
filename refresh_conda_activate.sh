#/bin/sh
echo Activating conda from myenv
conda activate myenv
# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, pip will install python packages"|| exit

./refresh.sh
