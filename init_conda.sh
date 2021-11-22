#/bin/sh
conda create --name myenv
echo If you answer Y environment will be refreshed (pip install, flask db upgrade, etc)
./check_continue.sh || exit
./refresh_conda.sh

