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
if test -f "myenv/bin/activate"
then
  chmod 700 myenv/bin/*
  chmod 700 myenv/bin/*.*
else
  chmod 700 myenv/Scripts/*
  chmod 700 myenv/Scripts/*.*
fi
