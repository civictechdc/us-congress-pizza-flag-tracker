echo Script will run the following commands:
echo .
echo 1. create_python_env.sh / create_conda_env.sh
echo 2. activate_python_env.sh / activate_conda_env.sh
echo 3. pip_install.sh \(long step, can be skipped\)
echo 4. db_schema.sh
echo 5. populate_seed_data.sh
echo 6. run.sh
echo
read -p "Press return or enter a step to start at: " -n1 answer
echo
if [ $answer\x == x ]; then
  step="1"
else
  step=$(uppercase.sh $answer)
fi
echo Starting step $step

env="python"
if [ $step -lt "3" ]; then
  read -p "(P)ython or (C)onda ? " -n1 answer
  echo
  if [ $answer == "C" -o $answer == "c" ]; then
    env=conda
  else
    env=python
  fi
  echo Env=$env
fi

if [ $step -le "4" ]; then
  read -p "Remove flag.db (Y/N) ? " -n1 answer
  echo
  if [ $answer == "Y" -o $answer == "y" ]; then
    rm flag.db
  fi
fi



if [ $step == "1" ];then
  create_$env\_env.sh 
fi

if [ $step -le "2" ];then
  source activate_$env\_env.sh
fi

if [ $step == "3" ]; then
  pip_install.sh
fi

if [ $step -lt "3" ]; then
  read -p "Run pip install (Y/N) ? " -n1 answer
  echo
  if [ $answer\x == Yx -o $answer\x == yx ]; then
    pip_install.sh
  fi
fi

( execute_step.sh 4 $step "db_schema.sh" "If you answer Y, db schema model changes will be applied." ] ) || exit
( execute_step.sh 5 $step populate_seed_data.sh "If you answer Y, data will be populated." ] ) || exit
( execute_step.sh 6 $step run.sh "If you answer Y, server will be started." ) || exit
