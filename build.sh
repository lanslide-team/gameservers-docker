#!/bin/bash
set -e

STARTT=$(date +%s.%N)

# ls csgo-base/csgo

mkdir -p /demos -m a+rwX
mkdir -p /opt/minecraft/plotworld -m a+rwX

docker image prune -f

export MYSQL_ROOT_PASSWORD=`echo -n l33t | sha256sum | base64 | head -c 32 ; echo`

docker pull mariadb:latest
docker start mariadb || docker run --name mariadb --network games -e MYSQL_ROOT_PASSWORD="$MYSQL_ROOT_PASSWORD" -d mariadb

docker build -t='base:latest' base/

docker build -t='amxx:latest' amxx/
docker build -t='sourcemod:latest' sourcemod/
docker build -t='counter-strike-sharp:latest' counter-strike-sharp
docker build -t='cs-base:latest' cs-base/ --no-cache
docker build -t='cs-venilla:latest' cs-vanilla/ --no-cache
docker build -t='cs-comp:latest' cs-comp/ --no-cache
docker build -t='css-base:latest' css-base/ --no-cache
docker build -t='css-venilla:latest' css-vanilla/ --no-cache
docker build -t='css-comp:latest' css-comp/ --no-cache
docker build -t='cs2-base:latest' cs2-base/
docker build -t='cs2-armsrace:latest' cs2-armsrace/ --no-cache
docker build -t='cs2-vanilla:latest' cs2-vanilla/
docker build -t='cs2-wingman-vanilla:latest' cs2-wingman-vanilla/ --no-cache
docker build -t='cs2-comp:latest' cs2-comp/
docker build -t='cs2-wingman:latest' cs2-wingman/

#docker build -t='csgo-base:latest' csgo-base/
#docker build -t='ls-warmod:latest' ls-warmod/
#docker build -t='csgo-comp:latest' csgo-comp/
#docker build -t='csgo-dm:latest' csgo-dm/
#docker build -t='csgo-ar:latest' csgo-ar/
#docker build -t='csgo-surf:latest' csgo-surf/
#docker build -t='csgo-wingman:latest' csgo-wingman/

docker build -t='wine:latest' wine/
docker build -t='wineconsole/lite:latest' wineconsole/

docker build -t='7days:latest' 7days/
docker build -t='altitude:latest' altitude/
docker pull factoriotools/factorio:latest
docker build -t='haloce:latest' haloce/
docker build -t='hl2:latest' hl2/
#docker build -t='l4d2:latest' l4d2/
docker build -t='minecraft:latest' minecraft/
docker build -t='minecraft-base:latest' minecraft-base/
docker build -t='minecraft-build:latest' minecraft-build/
docker build -t='minecraft-map:latest' minecraft-map/
docker build -t='retrocycles:latest' retrocycles/
docker build -t='ioquake3:latest' ioquake3/
docker build -t='reflex-arena:latest' reflex-arena/
docker build -t='rust:latest' rust/
docker pull wolveix/satisfactory-server:latest
docker build -t='tf2:latest' tf2/
docker build -t='trackmania-forever:latest' trackmania-forever/
docker build -t='trackmania-forever-rcon:latest' trackmania-forever-rcon/
docker build -t='ut2004:latest' ut2004/
docker build -t='ut99:latest' ut99/
docker build -t='wreckfest:latest' wreckfest/
docker build -t='zdaemon:latest' zdaemon/

docker image prune -f

ENDT=$(date +%s.%N)
printf "Time: "
echo "$ENDT - $STARTT" | bc
