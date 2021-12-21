step=$1
minimum_step=$2
command=$3
enter_y_n_text=$4

if [ $step -lt $minimum_step ];
then
  exit
fi

if [ $step -ne $minimum_step ]; then
  echo
  echo $enter_y_n_text
  read -p "Enter Y to continue, N to abort: " -n1 answer
  echo
  if [ "$answer" != "Y" -a "$answer" != "y" ]; then
    exit 1
  fi
fi

echo Running $command
$command

