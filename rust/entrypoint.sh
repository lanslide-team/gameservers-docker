#!/bin/bash

IDENTITY="${IDENTITY:-lanslide}"
IP="${IP:-0.0.0.0}"
PORT="${PORT:-28015}"
LEVEL="${LEVEL:-Procedural Map}"   # Procedural Map, Barren, HapisIsland, SavasIsland 
LOG_FILE="${LOG_FILE:-server.log}" # Using standard output for the moment
MAX_PLAYERS="${MAX_PLAYERS:-50}"
QUERY_PORT="${QUERY_PORT:-28017}"
SAVE_INTERVAL="${SAVE_INTERVAL:-300}"
SEED="${SEED:-235317}"             # range: 1-2147483647, used to reproduce a procedural map
SERVER_NAME="${SERVER_NAME:-LAN-slide Rust}"
TICK_RATE="${TICK_RATE:-30}"       # default: 30, range: 15-100
RCON_IP="${RCON_IP:-0.0.0.0}"
RCON_PORT="${RCON_PORT:-28016}"
RCON_PASSWORD="${RCON_PASSWORD:-lanslide}"
RCON_WEB="${RCON_WEB:-1}"          # 1 for the Facepunch web panel, Rustadmin desktop and Rustadmin Online;
WORLD_SIZE="${WORLD_SIZE:-3000}"   # default: 3000, range: 1000-6000, map size in meters

./RustDedicated +server.ip "${IP}" +server.port ${PORT} +server.hostname "${SERVER_NAME}" +server.identity "${IDENTITY}" +server.maxplayers ${MAX_PLAYERS} +server.saveinterval ${SAVE_INTERVAL} +server.seed ${SEED} +server.tickrate ${TICK_RATE} +server.worldsize ${WORLD_SIZE} +rcon.ip "${RCON_IP}" +rcon.port ${RCON_PORT} +rcon.password "${RCON_PASSWORD}" +rcon.web ${RCON_WEB} +query_port ${QUERY_PORT} -batchmode -logfile ${LOG_FILE} 

