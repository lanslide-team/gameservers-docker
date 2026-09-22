#!/bin/bash 

docker build -t='base:latest' base/
docker build -t='wine:latest' wine/
docker build -t='moria:latest' moria/

