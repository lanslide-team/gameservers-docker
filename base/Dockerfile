FROM ubuntu:22.04
ARG TZ="Etc/UTC"
RUN sed -i 's/archive.ubuntu.com/au.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt-get update  && apt-get dist-upgrade -y &&\
        apt-get install -y git gcc make unzip p7zip-full curl wget iproute2 vim-tiny bzip2 jq software-properties-common apt-transport-https python3 python3-pip libc6 lib32stdc++6 lib32gcc-s1 lib32z1 && \
        apt-get clean

RUN pip3 install asyncio opengsq rcon

RUN echo "$TZ" > /etc/timezone
RUN  ln -fs /usr/share/zoneinfo/$TZ /etc/localtime

