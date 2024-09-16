#!/bin/bash

current_date=$(date +"%Y%m%d")
LOGFILE="/home/ubuntu/bibleweb/logs/$current_date.log"

if ! pgrep -f "node" > /dev/null
    echo "[OK] React app ok at $(date)" >> $LOGFILE
then
    cd /home/ubuntu/bibleweb/
    make deploy
    echo "[NG] React app was down, restarted at $(date)" >> $LOGFILE
fi
