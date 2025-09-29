FROM ls-warmod as warmod
LABEL maintainer="LAN-slide"

FROM csgo-base

USER steam
WORKDIR /csgo

COPY --chown=steam:steam cfg /csgo/csgo/cfg

# Get sourcemod files
COPY --from=sourcemod --chown=steam:steam /csgo /csgo/csgo

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /csgo/

ENV PYTHONUNBUFFERED=0

ENTRYPOINT ["./entrypoint.py"]
