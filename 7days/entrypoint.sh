#!/bin/bash

SERVER_NAME="${SERVER_NAME:-LAN-slide}"
SERVER_DESCRIPTION="${SERVER_DESCRIPTION:-A 7 Days to Die Server}"
SERVER_WEBSITE_URL="${SERVER_WEBSITE_URL:-}"
SERVER_PASSWORD="${SERVER_PASSWORD:-}"
REGION="${REGION:-Oceania}"
SERVER_PORT="${SERVER_PORT:-26900}"
GAME_WORLD="${GAME_WORLD:-Navezgane}"
SERVER_VISIBILITY="${SERVER_VISIBILITY:-2}"                         # 2 = public, 1 = friends, 0 = Not listed,
SERVER_MAX_PLAYER_COUNT="${SERVER_MAX_PLAYER_COUNT:-32}"
GAME_NAME="${GAME_NAME:-My Game}"

sed -i "s/\$SERVER_NAME/$SERVER_NAME/" serverconfig.xml
sed -i "s/\$SERVER_DESCRIPTION/$SERVER_DESCRIPTION/" serverconfig.xml
sed -i "s/\$SERVER_WEBSITE_URL/$SERVER_WEBSITE_URL/" serverconfig.xml
sed -i "s/\$SERVER_PASSWORD/$SERVER_PASSWORD/" serverconfig.xml
sed -i "s/\$REGION/$REGION/" serverconfig.xml
sed -i "s/\$SERVER_PORT/$SERVER_PORT/" serverconfig.xml
sed -i "s/\$GAME_WORLD/$GAME_WORLD/" serverconfig.xml
sed -i "s/\$SERVER_VISIBILITY/$SERVER_VISIBILITY/" serverconfig.xml
sed -i "s/\$SERVER_MAX_PLAYER_COUNT/$SERVER_MAX_PLAYER_COUNT/" serverconfig.xml
sed -i "s/\$GAME_NAME/$GAME_NAME/" serverconfig.xml

hostname -i | python3 stats.py &

./startserver.sh -configfile=serverconfig.xml
