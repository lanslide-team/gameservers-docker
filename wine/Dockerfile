FROM base:latest

USER root

ARG DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y wget software-properties-common && \
    dpkg --add-architecture i386 && \
    mkdir -pm755 /etc/apt/keyrings && \
    wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key && \
    wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/noble/winehq-noble.sources && \
    wget -O /usr/local/bin/winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks && \
    chmod +x /usr/local/bin/winetricks && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends xvfb cabextract winehq-stable gosu && \
    mkdir /wineprefix-template && chown ls:ls /wineprefix-template && \
    runuser -l ls -c "WINEPREFIX=/wineprefix-template winecfg" && \
    sleep 5 && \
    runuser -l ls -c "WINEPREFIX=/wineprefix-template xvfb-run winetricks -q vcrun2022" && \
    rm -f /usr/local/bin/winetricks && \
    apt-get remove -y --purge wget xvfb cabextract software-properties-common && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN date -u +%Y%m%dT%H%M%SZ > /wineprefix-template/.timestamp

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8
