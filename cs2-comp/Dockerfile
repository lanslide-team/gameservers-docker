#FROM ls-warmod as warmod
#FROM sourcemod as sourcemod
FROM cs2-base
MAINTAINER LAN-slide

USER root
RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

# Get counter-strike-source files
COPY --from=counter-strike-sharp --chown=steam:steam /css /cs2/game/csgo
RUN sed -i "/Game_LowViolence/a\ \t\t\tGame\tcsgo/addons/metamod" /cs2/game/csgo/gameinfo.gi

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /cs2/
COPY --chown=steam:steam cfg /cs2/game/csgo/cfg

ENV PYTHONUNBUFFERED=0
RUN chmod +x entrypoint.py

ENTRYPOINT ["./entrypoint.py"]
