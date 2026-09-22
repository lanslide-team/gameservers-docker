FROM ubuntu:24.04
LABEL maintainer="LAN-slide"
ARG TZ="Etc/UTC"

RUN sed -i 's|archive.ubuntu.com|au.archive.ubuntu.com|g' /etc/apt/sources.list.d/ubuntu.sources

RUN userdel ubuntu && \
    groupadd -g 1000 ls && \
    useradd -m -u 1000 -g 1000 ls

# add-apt-repository ppa:jonathonf/vim
RUN apt-get update && apt-get install -y software-properties-common \
            git gcc make unzip p7zip-full curl wget iproute2 vim bzip2 jq \ 
            software-properties-common apt-transport-https python3 python3-pip libc6 \
            lib32stdc++6 lib32gcc-s1 lib32z1 libicu-dev && \
        apt-get install -y --no-install-recommends locales && \
        apt-get clean && \ 
    	echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
        locale-gen && \
        rm -rf /var/lib/apt/lists/*

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

ENV PIP_BREAK_SYSTEM_PACKAGES=1
RUN pip3 install opengsq rcon

RUN echo "$TZ" > /etc/timezone
RUN  ln -fs /usr/share/zoneinfo/$TZ /etc/localtime

