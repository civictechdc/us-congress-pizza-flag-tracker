#/bin/sh
echo Activating conda from myenv
conda activate myenv
echo Done

# ./check_continue.sh returns false if uses exit to exit
./check_continue.sh "If you answer Y main steps will be executed \(pip install, upgrade db, populate db)"

./refresh.sh
