#!/bin/bash
set -e

STARTT=$(date +%s.%N)

docker build -t='base:latest' base/
docker build -t='minecraft:latest' minecraft/ --no-cache
docker build -t='minecraft-base:latest' minecraft-base/ --no-cache
docker build -t='minecraft-build:latest' minecraft-build/ --no-cache
docker build -t='minecraft-map:latest' minecraft-map/ --no-cache

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
