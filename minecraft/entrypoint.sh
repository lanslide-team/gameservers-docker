#!/bin/sh

python3 /advertise.py "$SERVER_NAME" &
ip route get 1 | sed 's/^.*src \([^ ]*\).*$/\1/;q' | python3 /data/stats.py &

/start
