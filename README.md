# gameserver

## Files

- build.sh: Builds/Creates the docker images.
- delete.sh: Removes any docker containers (except for mariadb).
- delete\_images.sh: Remove any docker images.
- network.sh: Example of creating the **games** docker network.
- test.sh: Used to spin up multiple CS:GO servers
- update\_steam.sh: Downloads the game server files via steamcmd.

## Requirements

Ensure the following utilities are installed:

For example:
```
apt-get install git svn w3m wget unzip
dnf install docker git svn w3m wget unzip

You may need requirements for steamcmd:

apt install lib32gcc-s1 libc6-i386 lib32stdc++6 curl wget tar
dnf install glibc.i686 libstdc++.i686 curl wget tar
```

Docker should be enabled on startup.

``service docker enable``

## Clone the repository

We recommend cloning into your user's home directory.

``git clone git@gitlab.com:lanslide/gameserver.git``

## Download the game server files

This will download the additional server files, mainly from steamcmd.

``./update.sh``

## Setup the docker network

Create a docker network called ``games``.
Replace **subnet**, **ip-range**, **gateway**, and **parent** with the appropriate settings.

Note: No other clients should be allocated IPs in this range from any DHCP servers.

```
docker network create -d macvlan \
   --subnet=192.168.1.1/24 \
   --ip-range=192.168.1.128/25 \
   --gateway=192.168.1.1 \
   -o parent=enp37s0 games
```

## Run docker build script

This will download/create the docker images ready to create containers.

``./build.sh``

## Install python script

See python project page for more details: https://pypi.org/project/lsquery/

We recommend you install the script as a service, so it starts on boot.

## Test 

Goto the [LAN-slide Portal](https://portal.lanslide.com.au) to see if you can create game servers from the new host.
