#!/bin/bash
set -e

STARTT=$(date +%s.%N)

if [ "$1" != "cached" ]; then
	gs_root=`pwd`
	steamcmd=steamcmd
	login_user="stupidsteamlogin ssl_2022"

	${gs_root}/steamcmd/steamcmd.sh +force_install_dir ${gs_root}/cs2-base/data +login ${login_user} +app_update 730 +quit
fi

docker build -t='base:latest' base/
docker build -t='cs2-base:latest' cs2-base/ --no-cache
docker build -t='cs2-armsrace:latest' cs2-armsrace/ --no-cache
docker build -t='sourcemod:latest' sourcemod/
docker build -t='counter-strike-sharp:latest' counter-strike-sharp/ --no-cache
#docker build -t='ls-warmod:latest' ls-warmod/
docker build -t='cs2-vanilla:latest' cs2-vanilla/ --no-cache
docker build -t='cs2-wingman-vanilla:latest' cs2-wingman-vanilla/ --no-cache
docker build -t='cs2-comp:latest' cs2-comp/ --no-cache
#docker build -t='csgo-dm:latest' csgo-dm/
#docker build -t='csgo-ar:latest' csgo-ar/
#docker build -t='csgo-surf:latest' csgo-surf/
docker build -t='cs2-wingman:latest' cs2-wingman/

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
