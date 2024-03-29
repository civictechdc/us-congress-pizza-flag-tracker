#/bin/sh
pyv="$(python3 -V 2>&1)"

if [[ "$pyv" != *"command not found"* ]];
then
  echo Running pip3 install
  pycommand="python3"
else
  echo Running pip install
  pycommand="python"
fi

echo NOTE: if this takes more than about 2 minutes, you can use alternative below. See https://stackoverflow.com/questions/65122957/resolving-new-pip-backtracking-runtime-issue for one article on the issue.
echo .
echo . pip install -r requirements.txt --use-deprecated=legacy-resolver
echo .
$pycommand -m pip install -r requirements.txt
echo Done
