#!/bin/bash
set -euo pipefail

echo "[Wreckfest2] Starting container…"

ENV_VAR_ARR1='BBMETA_SERVER BBMETA_NET NAME DESCRIPTION PASSWORD LOG_FILE_NAME GAME_PORT BBMETA_GAME BBMETA_CUP POINT_DISTRIBUTION START_ORDER POINTS_FOR_BEST_LAP_TIME POINTS_FOR_HIGHEST_SCORE LAST_RACE_MULTIPLIER NUMBER_OF_RACES EVENT_LOOP_NAME COUNTDOWN_TIME GAME_FLAGS';
ENV_VAR_ARR2='BBMETA_LOOP BBMETA_EVENTS BBMETA_LEVEL LEVEL_ID WEATHER_PATH AI_SET_PATH GAME_MODE_ID BBMETA_RULES LAPS TIME_LIMIT NUMBER_OF_TEAMS MAX_NUMBER_OF_PARTICIPANTS RULES_FLAGS CAR_RESET_DELAY VEHICLE_DAMAGE_ID BOT_COUNT';

BBMETA_SERVER="${BBMETA_SERVER:-scnf v0 n1}"
BBMETA_NET="${BBMETA_NET:-ncnf v2 n1}"
NAME="${NAME:-Wreckfest 2 Server}"
DESCRIPTION="${DESCRIPTION:-Wreck dem all}"
PASSWORD="${PASSWORD:-}"
LOG_FILE_NAME="${LOG_FILE_NAME:-}"
GAME_PORT="${GAME_PORT:-30100}"

BBMETA_GAME="${BBMETA_GAME:-gcnf v3 n1}"

BBMETA_CUP="${BBMETA_CUP:-mros v1 n1}"
POINT_DISTRIBUTION="${POINT_DISTRIBUTION:-30;27;25;20;19;18;17;16;15;14;13;12;11;10;9;8;7;6;5;4;3;2;1;0}"
START_ORDER="${START_ORDER:-random}"
POINTS_FOR_BEST_LAP_TIME="${POINTS_FOR_BEST_LAP_TIME:-0}"
POINTS_FOR_HIGHEST_SCORE="${POINTS_FOR_HIGHEST_SCORE:-0}"
LAST_RACE_MULTIPLIER="${LAST_RACE_MULTIPLIER:-1}"
NUMBER_OF_RACES="${NUMBER_OF_RACES:-5}"

BBMETA_LOOP="${BBMETA_LOOP:-becl v0 n1}"
BBMETA_EVENTS="${BBMETA_EVENTS:-ecnf v0 n23}"
BBMETA_LEVEL="${BBMETA_LEVEL:-mlvl v1 n1}"
LEVEL_ID="${LEVEL_ID:-track07_1}"
WEATHER_PATH="${WEATHER_PATH:-default}"
AI_SET_PATH="${AI_SET_PATH:-ai-class-all.aist}"
GAME_MODE_ID="${GAME_MODE_ID:-bangerrace}"
BBMETA_RULES="${BBMETA_RULES:-evru v4 n1}"
LAPS="${LAPS:-3}"
TIME_LIMIT="${TIME_LIMIT:-3}"
NUMBER_OF_TEAMS="${NUMBER_OF_TEAMS:-1}"
MAX_NUMBER_OF_PARTICIPANTS="${MAX_NUMBER_OF_PARTICIPANTS:-24}"
RULES_FLAGS="${RULES_FLAGS:-}"
CAR_RESET_DELAY="${CAR_RESET_DELAY:-5}"
VEHICLE_DAMAGE_ID="${VEHICLE_DAMAGE_ID:-normal}"
BOT_COUNT="${BOT_COUNT:-0}"

EVENT_LOOP_NAME="${EVENT_LOOP_NAME:-default_loop}"
COUNTDOWN_TIME="${COUNTDOWN_TIME:-30000}"
GAME_FLAGS="${GAME_FLAGS:-leader enabled}"

SERVER_CFG1="/wreckfest2/save/server_config.scnf"
SERVER_CFG2="/wreckfest2/save/default_loop.becl"

# ---- Paths ----
SERVER_DIR="/wreckfest2"
PROTON_BIN="/proton/proton"

# ---- Proton / Wine env ----
export WINEPREFIX="${WINEPREFIX:-/compat}"
export STEAM_COMPAT_DATA_PATH="${STEAM_COMPAT_DATA_PATH:-/compat}"
export STEAM_COMPAT_CLIENT_INSTALL_PATH="${STEAM_COMPAT_CLIENT_INSTALL_PATH:-/proton/steam-client}"

# Disable noisy logging unless debugging
export PROTON_LOG="${PROTON_LOG:-1}"
export WINEDEBUG="${WINEDEBUG:--all}"

# ---- Sanity checks ----
if [[ ! -x "$PROTON_BIN" ]]; then
  echo "[ERROR] Proton launcher not found or not executable at: $PROTON_BIN" >&2
  exit 1
fi

if [[ ! -f "$SERVER_DIR/Wreckfest2.exe" ]]; then
  echo "[ERROR] Wreckfest2.exe not found in $SERVER_DIR" >&2
  ls -la "$SERVER_DIR"
  exit 1
fi

mkdir -p "$WINEPREFIX"

echo "[Wreckfest2] Using Proton: $PROTON_BIN"
echo "[Wreckfest2] Wine prefix: $WINEPREFIX"
echo "[Wreckfest2] Server dir: $SERVER_DIR"

cd "$SERVER_DIR"

for ENV_VAR in $ENV_VAR_ARR1
do
     sed -i "s/\$$ENV_VAR/${!ENV_VAR}/" $SERVER_CFG1
done

for ENV_VAR in $ENV_VAR_ARR2
do
     sed -i "s/\$$ENV_VAR/${!ENV_VAR}/" $SERVER_CFG2
done

# ---- Default args (can be overridden via docker run) ----
DEFAULT_ARGS=(
  "./Wreckfest2.exe"
  "--server"
  "--save-dir=save"
)

set +e
"$PROTON_BIN" run "${DEFAULT_ARGS[@]}" 2>&1 | tee -a /compat/proton-wreckfest2.log
rc=${PIPESTATUS[0]}
set -e

sleep infinity
