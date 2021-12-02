#/bin/sh
echo Creating conda / python in myenv
conda create --name myenv
# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, env will be activated"|| exit
./refresh_conda.sh
