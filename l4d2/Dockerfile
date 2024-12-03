FROM sourcemod
FROM base

MAINTAINER LAN-slide


RUN useradd steam && mkdir /l4d2 && chown steam:steam /l4d2

USER steam

COPY --chown=steam:steam data /l4d2
COPY --from=sourcemod --chown=steam:steam /sm /l4d2/left4dead2/

WORKDIR /l4d2

COPY --chown=steam:steam cfg/server.cfg left4dead2/cfg/server.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT /l4d2/entrypoint.sh
