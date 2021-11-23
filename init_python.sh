#/bin/sh
<<<<<<< HEAD
pyv="$(python3 -V 2>&1)"

if [[ "$pyv" != *"command not found"* ]];
then
  echo Using python3
  pycommand="python3"
else
  echo Using python
  pycommand="python"
fi
$pycommand -m venv myenv

=======
python3 -m venv myenv
echo If you answer Y environment will be refreshed \(pip install, flask db upgrade, etc\)
./check_continue.sh
>>>>>>> b48a377 (Minor changes)
./refresh_python.sh
