FROM base
LABEL maintainer="LAN-slide"

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y \
        libncurses5:i386 \
        libtinfo5:i386

RUN useradd steam && mkdir /hl2 && chown steam:steam /hl2

RUN mkdir -p /home/steam/.steam/sdk32

USER steam

COPY --chown=steam:steam data /hl2

WORKDIR /hl2

COPY --chown=steam:steam cfg/server.cfg hl2mp/cfg/server.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam stats.py stats.py
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk32/steamclient.so

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/hl2/entrypoint.sh"]
