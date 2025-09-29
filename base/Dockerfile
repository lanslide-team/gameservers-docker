FROM ubuntu:22.04
LABEL maintainer="LAN-slide"
ARG TZ="Etc/UTC"
RUN sed -i 's/archive.ubuntu.com/au.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt-get update  && apt-get dist-upgrade -y && apt-get install -y software-properties-common && add-apt-repository ppa:jonathonf/vim && \
        apt-get install -y git gcc make unzip p7zip-full curl wget iproute2 vim bzip2 jq software-properties-common apt-transport-https python3 python3-pip libc6 lib32stdc++6 lib32gcc-s1 lib32z1 libicu-dev && \
        apt-get clean

RUN apt-get update && apt-get install -y --no-install-recommends locales && \
    sed -i 's/^# *en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && rm -rf /var/lib/apt/lists/*

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

RUN pip3 install asyncio opengsq rcon

RUN echo "$TZ" > /etc/timezone
RUN  ln -fs /usr/share/zoneinfo/$TZ /etc/localtime

