#!/bin/sh
echo "Edit this script to change the path to ioquake3's dedicated server executable and which binary if you aren't on x86_64."
echo "Set the sv_dlURL setting to a url like http://yoursite.com/ioquake3_path for ioquake3 clients to download extra data."

# sv_dlURL needs to have quotes escaped like \"http://yoursite.com/ioquake3_path\" or it will be set to "http:" in-game.
# +set com_hunkmegs 64 "$@" 

BOT_ENABLE="${BOT_ENABLE:-0}"
BOT_MIN_PLAYERS="${BOT_MIN_PLAYERS:-0}"
DEDICATED="${DEDICATED:-1}"			# 0: listen server, 1: LAN, 2: ONLINE
GAME_TYPE="${GAME_TYPE:-0}"			# 0: deathmatch, 1: 1-on-1, 2: SP DM, 3: Team DM, 4: CTF
MAX_PLAYERS="${MAX_PLAYERS:-64}"
SERVER_NAME="${SERVER_NAME:-LAN-slide Q3 FFA}"
MAP="${MAP:-q3dm1}"
NEXT_MAP="${NEXT_MAP:-q3dm2}"
HUNK_MEMORY="${HUNK_MEMORY:-128}"
ALLOW_VOTE="${ALLOW_VOTE:-1}"
NET_PORT="${NET_PORT:-27960}"
EVENT="${EVENT:-LAN-slide}"
TIMELIMIT="${TIMELIMIT:-15}"
FRAGLIMIT="${FRAGLIMIT:-50}"

MOTD="Welcome to ${EVENT}"

RCON_PASSWORD="${RCON_PASSWORD:-lanslide}"
PASSWORD="${PASSWORD:-}"

SERVER_CFG="baseq3/server.cfg"

if [ "$PASSWORD" = "" ]; then
    SV_PRIVATECLIENTS=0
else
    SV_PRIVATECLIENTS=1
fi

sed -i "s/\$BOT_ENABLE/$BOT_ENABLE/" $SERVER_CFG
sed -i "s/\$MAX_PLAYERS/$MAX_PLAYERS/" $SERVER_CFG
sed -i "s/\$SERVER_NAME/$SERVER_NAME/" $SERVER_CFG
sed -i "s/\$MAP/$MAP/" $SERVER_CFG
sed -i "s/\$NEXT_MAP/$NEXT_MAP/" $SERVER_CFG
sed -i "s/\$RCON_PASSWORD/$RCON_PASSWORD/" $SERVER_CFG
sed -i "s/\$PASSWORD/$PASSWORD/" $SERVER_CFG
sed -i "s/\$SV_PRIVATECLIENTS/$SV_PRIVATECLIENTS/" $SERVER_CFG
sed -i "s/\$MOTD/$MOTD/" $SERVER_CFG
sed -i "s/\$TIMELIMIT/$TIMELIMIT/" $SERVER_CFG
sed -i "s/\$FRAGLIMIT/$FRAGLIMIT/" $SERVER_CFG
sed -i "s/\$GAME_TYPE/$GAME_TYPE/" $SERVER_CFG

hostname -I | python3 stats.py &

./ioq3ded.x86_64 +set dedicated $DEDICATED +set com_hunkmegs $HUNK_MEMORY +set fs_game baseq3 +exec server.cfg +g_gametype $GAME_TYPE +set bot_min_players $BOT_MIN_PLAYERS +set g_allowvote $ALLOW_VOTE +set net_port $NET_PORT
