#!/bin/bash
#docker rm -f $(docker ps -a -q)
docker rm -f $(docker ps -aq | grep -v -E $(docker ps -aq --filter='name=mariadb' | paste -sd "|" -))
