#/bin/sh
echo Activating Python from myenv

if test -f "myenv/bin/activate"
then
  echo Sourcing myenv/bin/activate
  source myenv/bin/activate
else
  echo Running myenv/Scripts/activate
  myenv/Scripts/activate
fi

