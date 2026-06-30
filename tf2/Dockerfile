FROM sourcemod
FROM base
LABEL maintainer="LAN-slide"

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y \
        libncurses5:i386 \
        libtinfo5:i386

RUN useradd steam && mkdir /tf2 && chown steam:steam /tf2
RUN mkdir -p /home/steam/.steam/sdk32

RUN dpkg --add-architecture i386; apt-get update;  apt-get install -y libstdc++6:i386 libcurl4-gnutls-dev:i386

USER steam

COPY --chown=steam:steam data /tf2
COPY --from=sourcemod --chown=steam:steam /sm /tf2/tf/

WORKDIR /tf2

COPY --chown=steam:steam cfg/server.cfg tf/cfg/server.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam stats.py stats.py
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk32/steamclient.so

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/tf2/entrypoint.sh"]
