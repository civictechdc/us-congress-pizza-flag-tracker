#/bin/sh
echo Activating Python from myenv
pyv="$(source myenv/bin/activate -V 2>&1)"
if [[ "$pyv" != *"command not found"* ]];
then
  source myenv/bin/activate
else
  .\myenv\Scripts\activate
fi

echo

./check_continue.sh "If you enter Y, pip will install python packages"|| exit

./refresh.sh
