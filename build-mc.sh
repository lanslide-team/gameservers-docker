#!/bin/bash
set -e

STARTT=$(date +%s.%N)
VERSION="v1.21.11"

docker pull ghcr.io/lanslide-team/minecraft-build:$VERSION
docker pull ghcr.io/lanslide-team/minecraft-map:$VERSION

docker tag ghcr.io/lanslide-team/minecraft-build:$VERSION minecraft-build:$VERSION
docker tag ghcr.io/lanslide-team/minecraft-map:$VERSION minecraft-map:$VERSION

docker rmi minecraft-base:$VERSION

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
