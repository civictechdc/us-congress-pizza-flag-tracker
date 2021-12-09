#/bin/sh
echo Activating Python from myenv
source myenv/bin/activate
echo

# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you answer Y conda and python env will be activated"

./refresh.sh
