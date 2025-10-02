FROM base
LABEL maintainer="LAN-slide"

# RUN apt-get update && apt-get install -y wget mysql-client

RUN useradd -lm steam && mkdir /cs2 && chown steam:steam /cs2

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false
ENV LD_LIBRARY_PATH="/cs2/game/bin/linuxsteamrt64:/cs2/game/csgo/bin/linuxsteamrt64"

RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

COPY --chown=steam:steam container.py data defaultenv.ini entrypoint.py stats.py ./
COPY --chown=steam:steam cfg ./game/csgo/cfg/
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk64/steamclient.so

ENV PYTHONUNBUFFERED=0
RUN chmod +x entrypoint.py
