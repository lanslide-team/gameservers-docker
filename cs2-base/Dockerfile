FROM base
LABEL maintainer="LAN-slide"

# RUN apt-get update && apt-get install -y wget mysql-client

RUN mkdir /cs2 && chown ls:ls /cs2

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false
ENV LD_LIBRARY_PATH="/cs2/game/bin/linuxsteamrt64:/cs2/game/csgo/bin/linuxsteamrt64"

RUN mkdir -p /game/csgo/replays && chown -R ls:ls  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER ls
WORKDIR /cs2

COPY --chown=ls:ls container.py data defaultenv.ini entrypoint.py stats.py ./
COPY --chown=ls:ls cfg ./game/csgo/cfg/
COPY --chown=ls:ls steamclient.so /home/ls/.steam/sdk64/steamclient.so

ENV PYTHONUNBUFFERED=0
RUN chmod +x entrypoint.py
