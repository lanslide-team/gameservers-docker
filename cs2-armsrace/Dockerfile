FROM cs2-base
MAINTAINER LAN-slide

USER root
RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /cs2/
COPY --chown=steam:steam cfg /cs2/game/csgo/cfg
#COPY --chown=steam:steam team-logos /cs2/game/csgo/resource/flash/econ/tournaments/teams

ENV PYTHONUNBUFFERED=0
RUN chmod +x entrypoint.py

ENTRYPOINT ["./entrypoint.py"]
