#!/bin/bash

ENV_VAR_ARR='SERVER_NAME RCON_PASSWORD SV_PASSWORD SV_LAN MP_TIMELIMIT'

SERVER_NAME="${SERVER_NAME:-LAN-slide HL2DM}"
MAX_PLAYERS="${MAX_PLAYERS:-8}"
PORT="${PORT:-27015}"
MAP="${MAP:-ctf_2fort}"
RCON_PASSWORD="${RCON_PASSWORD:-DEFAULT_ADMIN_PASSWORD}"
SV_PASSOWRD="${SV_PASSWORD:-}"
GAME="${GAME:-tf}"
SERVER_CFG="${GAME}/cfg/server.cfg"
SV_LAN="${SV_LAN:-1}"
MP_TIMELIMIT="${MP_TIMELIMIT:-30}"

for ENV_VAR in $ENV_VAR_ARR
do
     sed -i "s/\$$ENV_VAR/${!ENV_VAR}/" $SERVER_CFG
done

if [[ -n $MAPCYCLE ]]; then
    echo $MAPCYCLE >> /tf2/tf/cfg/mapcycle_custom.txt
    sed -i 's/\\n/\n/g' /tf2/tf/cfg/mapcycle_custom.txt
    echo "mapcyclefile mapcycle_custom.txt" >> /tf2/tf/cfg/server.cfg
fi

ip route get 1 | sed 's/^.*src \([^ ]*\).*$/\1/;q' | python3 stats.py &

./srcds_run -console -game ${GAME} +port ${PORT} +maxplayers ${MAX_PLAYERS} +maxplayers_override ${MAX_PLAYERS} +map ${MAP}
