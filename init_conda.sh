#/bin/sh
echo Creating conda / python in myenv
conda create --name myenv


# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you answer Y conda and python env will be activated"

./refresh_conda.sh
