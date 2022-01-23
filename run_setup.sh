SCRIPT_PATH=$PWD/setup
if [ "$PATH" != *"$SCRIPT_PATH" ];then
  echo Setting path
  PATH=$PATH:$SCRIPT_PATH
fi
source setup.sh
