#!/bin/bash
read -p "Enter Y to continue, N to abort: " -n1 ans
if [ "$ans" != "Y" -a "$ans" != "y" ];
then
  echo Script exit
  exit 1
fi
echo Script continue