#!/bin/bash

ENV_VAR_ARR='SERVER_NAME RCON_PASSWORD SV_PASSWORD SV_FLAGS Z_DIFFICULTY'

SERVER_NAME="${SERVER_NAME:-LAN-slide HL2DM}"
MAX_PLAYERS="${MAX_PLAYERS:-8}"
#PORT="${PORT:-27015}"
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

hostname -I | python3 stats.py &

python3 /l4d2/left4dead2/config_admins.py >> /l4d2/left4dead2/addons/sourcemod/configs/admins_simple.ini && rm /l4d2/left4dead2/config_admins.py -f

./srcds_run -debug -console -game ${GAME} +maxplayers ${MAX_PLAYERS} +maxplayers_override ${MAX_PLAYERS} +map ${MAP}
