#!/bin/bash

containers=$(docker ps | awk '{if(NR>1) print $1}')
let target_count=$1
let count=1

for container in $containers
do
	if [ $count = "$target_count" ];then
		docker exec -it $container /bin/bash
		exit;
	fi
	count=$((count+1))
done
