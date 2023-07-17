FROM ls-warmod as warmod
FROM sourcemod as sourcemod
FROM csgo-base
MAINTAINER LAN-slide

USER root
RUN mkdir -p /csgo/csgo/warmod && chown -R steam:steam  /csgo/csgo/warmod && chmod a+rwX /csgo/csgo/warmod

USER steam
WORKDIR /csgo

# Get sourcemod files
COPY --from=sourcemod --chown=steam:steam /csgo /csgo/csgo

# Get compiled sourcemod plugins
COPY --from=warmod --chown=steam:steam /ls-sourcemod/compiled/lanslide.smx /csgo/csgo/addons/sourcemod/plugins/
COPY --from=warmod --chown=steam:steam /ls-sourcemod/compiled/warmod.smx /csgo/csgo/addons/sourcemod/plugins/

COPY --chown=steam:steam cfg /csgo/csgo/cfg

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /csgo/

ENV PYTHONUNBUFFERED=0

ENTRYPOINT ["./entrypoint.py"]
