#!/bin/bash

STEAM_USER=stupidsteamlogin
STEAM_PASS=ssl_2022
DEFAULT_ADMIN_PASSWORD=lanslide

docker run --rm -it \
  --name stardew-test \
  --network games \
  -e SERVER_NAME="LAN-slide Stardew" \
  -e STEAM_USERNAME="$STEAM_USER" \
  -e STEAM_PASSWORD="$STEAM_PASS" \
  -e VNC_PASSWORD="$DEFAULT_ADMIN_PASSWORD" \
  -e API_KEY="$DEFAULT_ADMIN_PASSWORD" \
  stardew-valley:latest
