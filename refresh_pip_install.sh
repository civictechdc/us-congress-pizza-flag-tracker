#/bin/sh
echo Running pip install
echo NOTE: if this takes more than about 2 minutes, you can use alternative below. See https://stackoverflow.com/questions/65122957/resolving-new-pip-backtracking-runtime-issue for one article on the issue.
echo .
echo . pip install -r requirements.txt --use-deprecated=legacy-resolver
echo .
pip install -r requirements.txt
echo Done
