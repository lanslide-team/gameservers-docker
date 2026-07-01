FROM base:latest

LABEL maintainer="LAN-slide"

RUN useradd -m tm && \
    mkdir -p /tm && \
    chown -R tm:tm /tm

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

COPY entrypoint.sh /tm/entrypoint.sh
COPY playlist.xml /tm/UserData/Maps/MatchSettings/playlist.xml
COPY *.zip /tm

RUN chmod +x /tm/entrypoint.sh
RUN chown tm:tm /tm -R

USER tm

EXPOSE 2350/udp
EXPOSE 3450/udp

CMD ["./entrypoint.sh"]
