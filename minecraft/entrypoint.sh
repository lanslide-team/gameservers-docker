#!/bin/sh

python3.9 /advertise.py "$SERVER_NAME" &
ip route get 1 | sed 's/^.*src \([^ ]*\).*$/\1/;q' | python3.9 /data/stats.py &

/start
