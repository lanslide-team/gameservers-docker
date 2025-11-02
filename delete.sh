#!/bin/bash
#docker rm -f $(docker ps -a -q)
docker ps -aq | grep -vFf <(docker ps -aq --filter='name=mariadb') | xargs -r docker rm -f

