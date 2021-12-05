#!/bin/bash
pyv="$(python3 -V 2>&1)"

if [[ "$pyv" != *"command not found"* ]];
then
  echo Using python3
  pycommand="python3"
else
  echo Using python
  pycommand="python"
fi

$pyv populate_seed_data.py
