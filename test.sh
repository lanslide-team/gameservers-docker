#!/bin/bash

limit=1
if [ $# -gt 0 ]; then
    limit=$1
fi 

for (( i=1; i<=$limit; i++ ))
do
    id=`docker create --network "lanslide" -e "GAME_TYPE=0" -e "GAME_MODE=0" -e "MAXPLAYERS_OVERRIDE=14" -e "SERVER_NAME=LAN-slide CS:GO Server #${i}" -e "TICKRATE=128" -e "EVENT_NAME=LAN-slide" -e "TV_ENABLE=true" -e "TV_NAME=[TV] LAN-slide" -e "TV_TITLE=[TV] LAN-slide" -e "LS_CHALLONGE=2" -e "TEAM1=Unnamed #12" -e "TEAM2=Unnamed #8" "csgo-comp:latest"`
    docker start ${id}
done


#docker create --name "Main_2" --network "lanslide" --mount type=bind,source="/demos",target="/csgo/csgo/warmod"  -e "GAME_TYPE=0" -e "GAME_MODE=1" -e "MAXPLAYERS_OVERRIDE=14" -e "HOSTNAME=Laravel CS:GO Main #2 Unnamed #12 vs Unnamed #8" -e "TICKRATE=128" -e "STEAMTOKEN=66991BF39C75E7F6EF5F7D5A975717B3" -e "EVENT_NAME=Laravel v28.0" -e "TV_ENABLE=true" -e "TV_NAME=[TV] Laravel CS:GO Main #2 Unnamed #12 vs Unnamed #8" -e "TV_TITLE=[TV] Laravel CS:GO Main #2 Unnamed #12 vs Unnamed #8" -e "LS_CHALLONGE=2" -e "TEAM1=Unnamed #12" -e "TEAM2=Unnamed #8" "csgo-comp:dev"
