#!/bin/bash

SERVER_NAME="${SERVER_NAME:-LAN-slide HL2DM}"
MAX_PLAYERS="${MAX_PLAYERS:-8}"
PORT="${PORT:-27015}"
MAP="${MAP:-dm_overwatch}"
RCON_PASSWORD="${RCON_PASSWORD:-lanslide}"
SERVER_CFG=server.cfg
SV_PASSOWRD="${SV_PASSWORD:-}"
WINLIMIT="${WINLIMIT:-50}"
SV_LAN="${SV_LAN:-1}"

sed -i "s/\$RCON_PASSWORD/$RCON_PASSWORD/" hl2mp/cfg/server.cfg
sed -i "s/\$SERVER_NAME/$SERVER_NAME/" hl2mp/cfg/server.cfg
sed -i "s/\$SV_PASSWORD/$SV_PASSWORD/" hl2mp/cfg/server.cfg
sed -i "s/\$WINLIMIT/$WINLIMIT/" hl2mp/cfg/server.cfg

if [[ -n $MAPCYCLE ]]; then
    echo $MAPCYCLE >> /hl2/hl2mp/cfg/mapcycle_custom.txt
    sed -i 's/\\n/\n/g' /hl2/hl2mp/cfg/mapcycle_custom.txt
    echo "mapcyclefile mapcycle_custom.txt" >> /hl2/hl2mp/cfg/server.cfg

fi

hostname -I | python3 stats.py &

./srcds_run -console -game hl2mp +port ${PORT} +maxplayers ${MAX_PLAYERS} +maxplayers_override ${MAX_PLAYERS} +exec ${SERVER_CFG} +map ${MAP}
