#!/bin/sh
set -e

export SETTINGS_PATH="${SETTINGS_PATH:-/data/settings/server-settings.json}"

python3 /usr/local/bin/configure-settings.py

exec /init
