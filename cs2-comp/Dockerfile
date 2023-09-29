#FROM ls-warmod as warmod
#FROM sourcemod as sourcemod
FROM cs2-base
MAINTAINER LAN-slide

USER root
RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

# Get sourcemod files
# COPY --from=sourcemod --chown=steam:steam /cs2 /cs2/game/csgo

# Get compiled sourcemod plugins
#COPY --from=warmod --chown=steam:steam /ls-sourcemod/compiled/lanslide.smx /csgo/csgo/addons/sourcemod/plugins/
#COPY --from=warmod --chown=steam:steam /ls-sourcemod/compiled/warmod.smx /csgo/csgo/addons/sourcemod/plugins/

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /cs2/
COPY --chown=steam:steam cfg /cs2/game/csgo/cfg

ENV PYTHONUNBUFFERED=0
RUN chmod +x entrypoint.py

ENTRYPOINT ["./entrypoint.py"]
