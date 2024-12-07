#!/bin/bash

docker build -t='l4d2-base:latest' l4d2-base/
docker build -t='l4d2-vanilla:latest' l4d2-vanilla/ --no-cache
docker build -t='l4d2-super-versus' l4d2-super-versus/ --no-cache

docker image prune -f
