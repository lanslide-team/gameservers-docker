#FROM ls-warmod as warmod
#FROM sourcemod as sourcemod
FROM cs2-base
LABEL maintainer="LAN-slide"

USER root
RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

# Get counter-strike-source files
COPY --from=counter-strike-sharp --chown=steam:steam /css /cs2/game/csgo

RUN sed -i "/Game_LowViolence/a\ \t\t\tGame\tcsgo/addons/metamod" /cs2/game/csgo/gameinfo.gi

COPY --chown=steam:steam defaultenv.ini stats.py /cs2/

ENTRYPOINT ["./entrypoint.py", "vanilla"]
