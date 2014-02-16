#!/bin/bash

# Runs python script within virtualenv
# used by cron

cd /home/lacina/IdeaProjects/PoolWatch/
source /home/lacina/PoolWatchEnv/bin/activate

python "getpooldata.py"  2>&1 >> /poolsWatch.log