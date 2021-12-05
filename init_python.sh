#/bin/sh
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e5b60bac93655058362969d53e983eb182261f50
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

<<<<<<< HEAD
=======
python3 -m venv myenv
echo If you answer Y environment will be refreshed \(pip install, flask db upgrade, etc\)
./check_continue.sh
>>>>>>> b48a377 (Minor changes)
=======
>>>>>>> e5b60bac93655058362969d53e983eb182261f50
./refresh_python.sh
