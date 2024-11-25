#!/bin/bash
set -e

STARTT=$(date +%s.%N)

if [ "$1" != "cached" ]; then
	gs_root=`pwd`
        ${gs_root}/steamcmd/steamcmd.sh +force_install_dir ${gs_root}/css-base/data +login anonymous +app_update 232330 validate +quit
fi

docker build -t='base:latest' base/
docker build -t='css-base:latest' css-base/ --no-cache
docker build -t='css-vanilla:latest' css-vanilla/ --no-cache
docker build -t='sourcemod:latest' sourcemod/ --no-cache
docker build -t='css-comp:latest' css-comp/ --no-cache

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
