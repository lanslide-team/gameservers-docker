FROM base
MAINTAINER LAN-slide

RUN useradd steam && mkdir /hl2 && chown steam:steam /hl2

USER steam

COPY --chown=steam:steam data /hl2

WORKDIR /hl2

COPY --chown=steam:steam cfg/server.cfg hl2mp/cfg/server.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT /hl2/entrypoint.sh
