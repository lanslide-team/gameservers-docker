#!/bin/bash

ENV_VAR_ARR='SERVER_NAME WELCOME_MESSAGE GAME_PASSWORD MAX_PLAYERS STEAM_PORT GAME_PORT QUERY_PORT EXCLUDE_FROM_QUICKPLAY CLEAR_USERS OWNER_DISABLED ADMIN_COUNTDOWN LOBBY_COUNTDOWN READY_PLAYERS_REQUIRED ADMIN_STEAM_IDS SESSION_MODE GRID_ORDER ENABLE_TRACK_VOTE DISABLE_IDLE_KICK TRACK GAMEMODE BOTS AI_DIFFICULTY NUM_TEAMS LAPS TIME_LIMIT ELIMINATION_INTERVAL VEHICLE_DAMAGE CAR_CLASS_RESTRICTION CAR_RESTRICTION SPECIAL_VEHICLES_DISABLED CAR_RESET_DISABLED CAR_RESET_DELAY WRONG_WAY_LIMITER_DISABLED WEATHER FREQUENCY MODS LOG'
SERVER_CFG=server_config.cfg

SERVER_NAME="${SERVER_NAME:-Wreckfest Server}"
WELCOME_MESSAGE="${WELCOME_MESSAGE:-Wreck them all}"
GAME_PASSWORD="${GAME_PASSWORD:-}"
MAX_PLAYERS="${MAX_PLAYERS:-32}"

STEAM_PORT="${STEAM_PORT:-27015}"
GAME_PORT="${GAME_PORT:-33540}"
QUERY_PORT="${QUERY_PORT:-27016}"

EVENT_LOOP_TRACKS="${EVENT_LOOP_TRACKS:-'gravel1_main_loop,tarmac1_main_circuit,speedway2_demolition_arena'}"
EVENT_LOOP_GAMEMODES="${EVENT_LOOP_GAMEMODES:-racing,racing,derby deathmatch}"

EXCLUDE_FROM_QUICKPLAY="${EXCLUDE_FROM_QUICKPLAY:-0}"
CLEAR_USERS="${CLEAR_USERS:-1}"
OWNER_DISABLED="${OWNER_DISABLED:-1}"
ADMIN_COUNTDOWN="${ADMIN_COUNTDOWN:-0}"
LOBBY_COUNTDOWN="${LOBBY_COUNTDOWN:-30}"
READY_PLAYERS_REQUIRED="${READY_PLAYERS_REQUIRED:-50}"
ADMIN_STEAM_IDS="${ADMIN_STEAM_IDS:-}"
SESSION_MODE="${SESSION_MODE:-normal}"       	   # normal, qualify-sprint, qualify-lap, 30p-aggr, 25p-aggr, 25p-mod, 24p-lin, 16p-lin, 10p-double, 10p-lin, 35p-folk, f1-1991, f1-2003, f1-2010, player_count_1]
GRID_ORDER="${GRID_ORDER:-perf_normal}"      	   # random, perf_normal, perf_reverse, qualifying, cup_normal, cup_reverse
ENABLE_TRACK_VOTE="${ENABLE_TRACK_VOTE:-1}"
DISABLE_IDLE_KICK="${DISABLE_IDLE_KICK:-0}"
TRACK="${TRACK:-speedway2_demolition_arena}"       # see tracks command
GAMEMODE="${GAMEMODE:-derby deathmatch}"     	   # racing, derby, derby deathmatch, team derby, team race, elimination race
BOTS="${BOTS:-0}"
AI_DIFFICULTY="${AI_DIFFICULTY:-amateur}"    	   # novice, amateur, expert
NUM_TEAMS="${NUM_TEAMS:-2}"                  	   # 2-4
LAPS="${LAPS:-3}"			     	   # 1-60
TIME_LIMIT="${TIME_LIMIT:-5}"
ELIMINATION_INTERVAL="${ELIMINATION_INTERVAL:-0}"  # 0, 20, 30, 45, 60, 90, 120
VEHICLE_DAMAGE="${VEHICLE_DAMAGE:-normal}"	   # normal, intense, realistic or extremenormal, intense, realistic or extreme
CAR_CLASS_RESTRICTION="${CAR_CLASS_RESTRCITION:-}" # blank, a, b, c
CAR_RESTRICTION="${CAR_RESTRICTION:-}"             # see cars command
SPECIAL_VEHICLES_DISABLED="${SPECIAL_VEHICLES_DISABLED:-0}"
CAR_RESET_DISABLED="${CAR_RESET_DISABLED:-0}"
CAR_RESET_DELAY="${CAR_RESET_DELAY:-0}"            # 0, 1-20
WRONG_WAY_LIMITER_DISABLED="${WRONG_WAY_LIMITER_DISABLED:-0}"
WEATHER="${WEATHER:-}"				   # see weather command
FREQUENCY="${FREQUENCY:-high}"			   # low / high
MODS="${MODS:-}"
LOG="${LOG:-log.txt}"

for ENV_VAR in $ENV_VAR_ARR
do
     sed -i "s/\$$ENV_VAR/${!ENV_VAR}/" $SERVER_CFG
done

# Add in event loop
IFS="," read -a loop_tracks <<< $EVENT_LOOP_TRACKS
IFS="," read -a loop_modes <<< $EVENT_LOOP_GAMEMODES

if [ ${#loop_tracks[@]} -ne ${#loop_modes[@]} ]; then
    echo "Mismatched Tracks[${#loop_tracks[@]}] and Modes [${#loop_modes[@]}]. Kill container and rebuild configuration"
    exit 1
else
    TRACK_COUNT=${#loop_tracks[@]}
fi;

for (( i = 0; i < "$TRACK_COUNT"; i++))
do

cat << EOF >> $SERVER_CFG

## Add Track Number ${i}
el_add=${loop_tracks[i]}
el_gamemode=${loop_modes[i]}
EOF

done

exec wine Wreckfest.exe -s server_config=$SERVER_CFG
