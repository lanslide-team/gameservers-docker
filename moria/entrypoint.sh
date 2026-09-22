#!/bin/bash

SERVER_CFG=MoriaServerConfig.ini
ENV_VAR_ARR='NAME TYPE SEED DIFFICULTY_PRESET CUSTOM_COMBAT_MULTIPLIER CUSTOM_ENEMY_AGGRESSION CUSTOM_SURVIVAL_DIFFICULTY CUSTOM_MINING_DROPS CUSTOM_WORLD_DROPS CUSTOM_HORDE_FREQUENCY CUSTOM_SIEGE_FREQUENCY CUSTOM_PETROL_FREQUENCY DLC LOADED_AREAS_LIMIT WORLD'

NAME=${NAME:-Moria Server}
TYPE=${TYPE:-campaign}
SEED=${SEED:-random}
DIFFICULTY_PRESET=${DIFFICULTY_PRESET:-campaign}
CUSTOM_COMBAT_MULTIPLIER=${CUSTOM_COMBAT_MULTIPLIER:-default}
CUSTOM_ENEMY_AGGRESSION=${CUSTOM_ENEMY_AGGRESSION:-default}
CUSTOM_SURVIVAL_DIFFICULTY=${CUSTOM_SURVIVAL_DIFFICULTY:-default}
CUSTOM_MINING_DROPS=${CUSTOM_MINING_DROPS:-default}
CUSTOM_WORLD_DROPS=${CUSTOM_WORLD_DROPS:-default}
CUSTOM_HORDE_FREQUENCY=${CUSTOM_HORDE_FREQUENCY:-default}
CUSTOM_SIEGE_FREQUENCY=${CUSTOM_SIEGE_FREQUENCY:-default}
CUSTOM_PETROL_FREQUENCY=${CUSTOM_PETROL_FREQUENCY:-default}
DLC=${DLC:-}
LOADED_AREAS_LIMIT=${LOADED_AREAS_LIMIT:-32}
WORLD=${WORLD:-}

for ENV_VAR in $ENV_VAR_ARR
do
     sed -i "s/\$$ENV_VAR/${!ENV_VAR}/" $SERVER_CFG
done

if [ -f /moria/Moria/Binaries/Win64/MoriaServer-Win64-Shipping.bak ]; then
    echo "[entrypoint] Restoring patched MoriaServer-Win64-Shipping.exe for steam validation"
    rm -f /moria/Moria/Binaries/Win64/MoriaServer-Win64-Shipping.exe
    mv /moria/Moria/Binaries/Win64/MoriaServer-Win64-Shipping.bak /server/Moria/Binaries/Win64/MoriaServer-Win64-Shipping.exe
fi

MODS_DIR="/moria/mods"
PAKS_DIR="/moria/Moria/Content/Paks"

mkdir -p "$PAKS_DIR"

for zip in "$MODS_DIR"/*.zip; do
    [ -e "$zip" ] || continue

    echo "Extracting $(basename "$zip")..."

    TMP_DIR=$(mktemp -d)

    unzip -o "$zip" -d "$TMP_DIR"

    # Move contents of the ZIP's top-level directory into Paks
    find "$TMP_DIR" -mindepth 1 -maxdepth 1 -type d -exec sh -c '
        cp -a "$1"/. "$2"/
    ' _ {} "$PAKS_DIR" \;

    # Also handle files directly in the ZIP
    find "$TMP_DIR" -mindepth 1 -maxdepth 1 -type f -exec cp -a {} "$PAKS_DIR"/ \;

    rm -rf "$TMP_DIR"
done

rm $MODS_DIR -rf

echo "Mods extracted."

exec "$@"

echo "[entrypoint] Patching subsystem in MoriaServer-Win64-Shipping.exe..."
patcher /moria/Moria/Binaries/Win64/MoriaServer-Win64-Shipping.exe

echo "[entrypoint] Launching wine Return to Moria..."
exec wine "/moria/Moria/Binaries/Win64/MoriaServer-Win64-Shipping.exe" Moria \
    "-NumServerWorkerThreads=${SERVER_WORKER_THREADS:-4}" \
    2>&1 | tee -a /moria/moria-server.log
