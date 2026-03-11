#!/usr/bin/env bash
set -euo pipefail

PORT=25565
DEFAULT_ALLOWED_SUBNET="10.20.93.0/24"
DEFAULT_CONTAINER=$(docker ps -q | head -n 1)

echo "Running containers:"
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Image}}"
echo

read -r -p "Enter container ID or name [default: $DEFAULT_CONTAINER]: " CONTAINER
CONTAINER=${CONTAINER:-$DEFAULT_CONTAINER}

[ -n "$CONTAINER" ] || { echo "No running containers found."; exit 1; }

PID=$(docker inspect -f '{{.State.Pid}}' "$CONTAINER")
IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$CONTAINER")

read -r -p "Allowed subnet [default: $DEFAULT_ALLOWED_SUBNET]: " ALLOWED_SUBNET
ALLOWED_SUBNET=${ALLOWED_SUBNET:-$DEFAULT_ALLOWED_SUBNET}

echo "Container: $CONTAINER"
echo "PID: $PID"
echo "IP: $IP"
echo "Allowed subnet: $ALLOWED_SUBNET"
echo

read -r -p "Action? (add/remove/show): " ACTION

case "$ACTION" in
  add)
    sudo nsenter -t "$PID" -n iptables -I INPUT 1 -p tcp -s "$ALLOWED_SUBNET" --dport "$PORT" -j ACCEPT
    sudo nsenter -t "$PID" -n iptables -I INPUT 2 -p tcp --dport "$PORT" -j DROP
    echo "Rules added."
    ;;
  remove)
    sudo nsenter -t "$PID" -n iptables -D INPUT -p tcp -s "$ALLOWED_SUBNET" --dport "$PORT" -j ACCEPT || true
    sudo nsenter -t "$PID" -n iptables -D INPUT -p tcp --dport "$PORT" -j DROP || true
    echo "Rules removed."
    ;;
  show)
    sudo nsenter -t "$PID" -n iptables -L INPUT -n -v --line-numbers
    ;;
  *)
    echo "Invalid action."
    exit 1
    ;;
esac
