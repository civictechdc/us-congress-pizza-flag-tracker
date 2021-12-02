#/bin/sh
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

# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you enter Y, python will be activated"|| exit

./refresh_python.sh
