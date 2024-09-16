#!/bin/bash

delaytime=${1:-0}
sleep $delaytime

current_date=$(date +"%Y%m%d")
LOGFILE="/home/ubuntu/bibleweb/logs/$current_date.log"
LOCK="/home/ubuntu/bibleweb/logs/LOCK"

if [ ! -f $LOCK ]; then
    touch $LOCK

    if pgrep -f "node" > /dev/null
    then
        echo "[OK][$delaytime] React app ok at $(date)" >> $LOGFILE
    else
        cd /home/ubuntu/bibleweb/
        make deploy
        echo "[NG][$delaytime] React app was down, restarted at $(date)" >> $LOGFILE
    fi

    rm $LOCK
else
    echo "[WARN][$delaytime] Lock file exists. Skipping execution at $(date)" >> $LOGFILE
fi
