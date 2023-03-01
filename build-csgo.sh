#!/bin/bash
set -e

STARTT=$(date +%s.%N)

# ls csgo-base/csgo

docker build -t='csgo-base:latest' csgo-base/
docker build -t='sourcemod:latest' sourcemod/
docker build -t='ls-warmod:latest' ls-warmod/
docker build -t='csgo-comp:latest' csgo-comp/
docker build -t='csgo-dm:latest' csgo-dm/
docker build -t='csgo-ar:latest' csgo-ar/
docker build -t='csgo-surf:latest' csgo-surf/
docker build -t='csgo-wingman:latest' csgo-wingman/

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
