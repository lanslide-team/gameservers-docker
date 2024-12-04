#!/bin/bash

ENV_VAR_ARR='SERVER_NAME RCON_PASSWORD SV_PASSWORD SV_FLAGS Z_DIFFICULTY'

SERVER_NAME="${SERVER_NAME:-LAN-slide HL2DM}"
MAX_PLAYERS="${MAX_PLAYERS:-8}"
PORT="${PORT:-27015}"
MAP="${MAP:-c1m4_atrium}"
RCON_PASSWORD="${RCON_PASSWORD:-lanslide}"
SV_PASSOWRD="${SV_PASSWORD:-}"
SV_FLAGS="${SV_FLAGS:-Browser}"
GAME_MODE="${GAME_MODE:-versus}"
Z_DIFFICULTY="${Z_DIFFICULTY:-normal}"
GAME="${GAME:-left4dead2}"
SV_LAN="${SV_LAN:-1}"
SERVER_CFG="${GAME}/cfg/server.cfg"

for ENV_VAR in $ENV_VAR_ARR
do
     sed -i "s/\$$ENV_VAR/${!ENV_VAR}/" $SERVER_CFG
done


#if [[ -n $MAPCYCLE ]]; then
#    echo $MAPCYCLE >> /hl2/hl2mp/cfg/mapcycle_custom.txt
#    sed -i 's/\\n/\n/g' /hl2/hl2mp/cfg/mapcycle_custom.txt
#    echo "mapcyclefile mapcycle_custom.txt" >> /hl2/hl2mp/cfg/server.cfg
#fi

hostname -i | python3 stats.py &

./srcds_run -console -game ${GAME} +port ${PORT} +maxplayers ${MAX_PLAYERS} +maxplayers_override ${MAX_PLAYERS} +map ${MAP}
