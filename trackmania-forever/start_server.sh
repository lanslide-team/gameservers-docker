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

RCON_MD5="$(printf '%s' "$RCON_PASSWORD" | md5sum | awk '{print $1}')"
sed -i "s|^[[:space:]]*const[[:space:]]\+PASSWORD[[:space:]]*=[[:space:]]*'.*';|      const PASSWORD = '${RCON_MD5}';|" \
  /var/www/html/config/adminserv.cfg.php

echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf
a2enconf servername >/dev/null 2>&1 || true

echo "Starting apache"
apachectl -D FOREGROUND &

echo "Starting apache server"
service apache2 start

echo "Server config dedicated_cfg.txt is"
cat $dedicated_cfg

sed -i "s/\$TRACK/${TRACK/\\/\\\\}/" $tracklist_root/tracklist-custom.cfg


echo "Launching server"
exec ./TrackmaniaServer /lan /game_settings=$TRACKLIST /dedicated_cfg=dedicated_cfg.txt /nodaemon

