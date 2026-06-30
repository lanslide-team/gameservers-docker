FROM sourcemod
FROM base

LABEL maintainer="LAN-slide"

RUN useradd steam && mkdir /l4d2 && chown steam:steam /l4d2
RUN apt-get update && apt-get install -y gdb
RUN mkdir -p /home/steam/.steam/sdk32

USER steam

COPY --chown=steam:steam data /l4d2
COPY --from=sourcemod --chown=steam:steam /sm /l4d2/left4dead2/

WORKDIR /l4d2

COPY --chown=steam:steam stats.py stats.py
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk32/steamclient.so
