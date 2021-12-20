#!/bin/bash
echo
echo "*** CHECK ABOVE FOR ERRORS ***"
echo
echo $1
echo
read -p "Enter Y to continue, N to abort: " -n1 answer
echo
# -a is shell script for AND
if [ "$answer" != "Y" -a "$answer" != "y" ];
then
  exit 1
fi
 