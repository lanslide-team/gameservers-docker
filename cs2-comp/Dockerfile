FROM cs2-base
LABEL maintainer="LAN-slide"

USER root
RUN mkdir -p /cs2/game/csgo/replays && chown -R steam:steam  /cs2/game/csgo/replays && chmod a+rwX /cs2/game/csgo/replays

WORKDIR /cs2

# Get counter-strike-source files
COPY --from=counter-strike-sharp --chown=steam:steam /config_admins.py /cs2
COPY --from=counter-strike-sharp --chown=steam:steam /config_match.py /cs2
COPY --from=counter-strike-sharp --chown=steam:steam /config_whitelist.py /cs2
COPY --from=counter-strike-sharp --chown=steam:steam /css /cs2/game/csgo

USER steam

RUN sed -i "/Game_LowViolence/a\ \t\t\tGame\tcsgo/addons/metamod" /cs2/game/csgo/gameinfo.gi

COPY --chown=steam:steam defaultenv.ini stats.py /cs2/
COPY --chown=steam:steam team-logos /cs2/game/csgo/resource/flash/econ/tournaments/teams
RUN rm -rf /cs2/game/csgo/cfg/gamemode_competitive.cfg

ENTRYPOINT ["./entrypoint.py", "comp"]
