#/bin/sh
python3 -m venv myenv
echo If you answer Y environment will be refreshed \(pip install, flask db upgrade, etc\)
./check_continue.sh
./refresh_python.sh
