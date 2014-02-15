#!/bin/bash

# Runs python script within virtualenv
# used by cron

cd `dirname $0`
source /home/lacina/PoolWatchEnv/bin/activate
python "${@:1}"