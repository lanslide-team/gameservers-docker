FROM base:latest

LABEL maintainer="LAN-slide"

RUN mkdir -p /tm && chown -R ls:ls /tm

RUN apt-get update && \
    apt-get install -y \
        wget \
        unzip \
        libicu-dev \
        xmlstarlet && \
    apt-get clean

WORKDIR /tm

RUN wget -O TrackmaniaServer_Latest.zip \
    http://files.v04.maniaplanet.com/server/TrackmaniaServer_Latest.zip && \
    unzip TrackmaniaServer_Latest.zip && \
    rm -f TrackmaniaServer_Latest.zip

RUN wget -O TM2020-Gamemodes-master.zip \
    https://git.virtit.fr/beu/TM2020-Gamemodes/archive/master.zip && \
    unzip TM2020-Gamemodes-master.zip -d /tmp && \
    mkdir -p /tm/UserData/Scripts && \
    cp -a /tmp/tm2020-gamemodes/*.Script.txt /tm/UserData/Scripts/ && \
    cp -a /tmp/tm2020-gamemodes/Libs /tm/UserData/Scripts/ && \
    rm -rf /tmp/tm2020-gamemodes TM2020-Gamemodes-master.zip

COPY entrypoint.sh /tm/entrypoint.sh
COPY playlist.xml /tm/UserData/Maps/MatchSettings/playlist.xml
COPY restartmap.py /tm/restartmap.py
COPY *.zip /tm

RUN chmod +x /tm/entrypoint.sh && \
    chown -R ls:ls /tm

USER ls

EXPOSE 2350/udp
EXPOSE 3450/udp

CMD ["./entrypoint.sh"]
