FROM sourcemod
FROM base


RUN useradd steam && mkdir /tf2 && chown steam:steam /tf2

RUN dpkg --add-architecture i386; apt-get update;  apt-get install -y libstdc++6:i386 libcurl4-gnutls-dev:i386

USER steam

COPY --chown=steam:steam data /tf2
COPY --from=sourcemod --chown=steam:steam /cs2 /tf2/tf/

WORKDIR /tf2

COPY --chown=steam:steam cfg/server.cfg tf/cfg/server.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT /tf2/entrypoint.sh
