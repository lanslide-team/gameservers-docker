#!/bin/bash
set -e

STARTT=$(date +%s.%N)

if [ "$1" != "cached" ]; then
	gs_root=`pwd`
        ${gs_root}/steamcmd/steamcmd.sh +force_install_dir ${gs_root}/cs-base/data +login anonymous +app_set_config 90 mod cstrike +app_update 90 -beta steam_legacy validate +quit
fi

docker build -t='base:latest' base/
docker build -t='cs-base:latest' cs-base/ --no-cache
docker build -t='cs-vanilla:latest' cs-vanilla/ --no-cache
docker build -t='amxx:latest' amxx/ --no-cache
docker build -t='cs-comp:latest' cs-comp/ --no-cache

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
