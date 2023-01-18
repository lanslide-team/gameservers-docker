#!/bin/bash
set -e

grep -E '^ID=' /etc/os-release | grep -q centos
if [ $? -eq 0 ]; then
    yum install -y glibc.i686 libstdc++.i686
fi

grep -E '^ID=' /etc/os-release | grep -q -E 'debian|ubuntu'
if [ $? -eq 0 ]; then
    sudo apt-get install -y lib32gcc1
fi

mkdir Steam && cd Steam
curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -
