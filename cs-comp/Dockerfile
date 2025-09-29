FROM cs-base
LABEL maintainer="LAN-slide"

USER root

WORKDIR /cs

COPY --from=amxx --chown=steam:steam /amxx/addons /cs/cstrike/addons
COPY --from=amxx --chown=steam:steam /amxx/config_admins.py /cs
#COPY --from=amxx --chown=steam:steam /amxx/config_admins_mb.py /cs
COPY --from=amxx --chown=steam:steam /amxx/rehlds/bin/linux32/engine_i486.so /cs/
COPY --from=amxx --chown=steam:steam /amxx/regamedllcs/bin/linux32/cstrike /cs/cstrike
#COPY --from=amxx --chown=steam:steam /amxx/regamedllcs/dist /cs/cstrike
#COPY --from=amxx --chown=steam:steam /amxx/matchbot /cs/cstrike
COPY --chown=steam:steam entrypoint.py /cs/
COPY --chown=steam:steam cfg /cs/cstrike
COPY --from=amxx --chown=steam:steam /amxx/match-deluxe/addons /cs/cstrike/addons

RUN sed -i 's|gamedll_linux "dlls/cs.so"|gamedll_linux "addons/metamod/metamod_i386.so"|g' /cs/cstrike/liblist.gam
RUN echo "\namx_match_deluxe.amxx\n" >> "/cs/cstrike/addons/amxmodx/configs/plugins.ini" 

USER steam

RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
