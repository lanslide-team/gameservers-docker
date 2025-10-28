#!/bin/bash
set -e

STARTT=$(date +%s.%N)
VERSION="v1.21.10"

docker pull ghcr.io/lanslide-team/spigot-build:$VERSION
docker pull ghcr.io/lanslide-team/spigot-map:$VERSION

docker tag ghcr.io/lanslide-team/spigot-build:$VERSION minecraft-build:$VERSION
docker tag ghcr.io/lanslide-team/spigot-map:$VERSION minecraft-map:$VERSION

docker rmi ghcr.io/lanslide-team/spigot-build:$VERSION
docker rmi ghcr.io/lanslide-team/spigot-map:$VERSION

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
