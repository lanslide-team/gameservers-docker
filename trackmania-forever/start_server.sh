#!/bin/bash

dedicated_cfg="/tm/GameData/Config/dedicated_cfg.txt"
tracklist_root="/tm/GameData/Tracks"

[[ -n $RCON_PASSWORD ]] || RCON_PASSWORD=$(dd if=/dev/urandom bs=20 count=1 2>/dev/null | base64)

sed -i "s/%%SERVER_NAME%%/$SERVER_NAME/" $dedicated_cfg
sed -i "s/SuperAdminPassword/$RCON_PASSWORD/" $dedicated_cfg
sed -i "s/AdminPassword/$RCON_PASSWORD/" $dedicated_cfg
sed -i "s/UserPassword/$RCON_PASSWORD/" $dedicated_cfg
[[ -n $TRACK ]] || TRACK="Green\B11-Race.Challenge"
[[ -n $TRACKLIST ]] || TRACKLIST="tracklist-all.cfg"

echo "Starting apache server"
service apache2 start

echo "Server config dedicated_cfg.txt is"
cat $dedicated_cfg

sed -i "s/\$TRACK/${TRACK/\\/\\\\}/" $tracklist_root/tracklist-custom.cfg

echo "Launching server"
exec ./TrackmaniaServer /lan /game_settings=$TRACKLIST /dedicated_cfg=dedicated_cfg.txt /nodaemon

