#!/bin/bash

containers=$(docker ps | awk '{if(NR>1) print $NF}')
let target_i=$1-1

for i in "${!containers[@]}"
do
	if [ $i -eq "$target_i" ];then
		docker exec -it ${containers[$i]} /bin/bash
		exit;
	fi
done
