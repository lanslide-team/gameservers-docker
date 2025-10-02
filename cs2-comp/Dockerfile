FROM cs2-base
LABEL maintainer="LAN-slide"

# Get counter-strike-source files
COPY --from=counter-strike-sharp --chown=steam:steam /config_admins.py /cs2
COPY --from=counter-strike-sharp --chown=steam:steam /config_match.py /cs2
COPY --from=counter-strike-sharp --chown=steam:steam /config_whitelist.py /cs2
COPY --from=counter-strike-sharp --chown=steam:steam /css /cs2/game/csgo

RUN sed -i "/Game_LowViolence/a\ \t\t\tGame\tcsgo/addons/metamod" /cs2/game/csgo/gameinfo.gi

COPY --chown=steam:steam team-logos /cs2/game/csgo/resource/flash/econ/tournaments/teams
# RUN rm -rf /cs2/game/csgo/cfg/gamemode_competitive.cfg

ENTRYPOINT ["./entrypoint.py", "comp"]
