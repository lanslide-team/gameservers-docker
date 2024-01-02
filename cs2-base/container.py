#!/usr/bin/python3

with open( '/proc/self/mountinfo' ) as file:
    line = file.readline().strip()
    while line:
        if '/docker/containers/' in line:
            containerID = line.split('/docker/containers/')[-1]     # Take only text to the right
            containerID = containerID.split('/')[0]                 # Take only text to the left
            break
        line = file.readline().strip()

    print(containerID)
