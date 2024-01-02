FROM cs2-base
MAINTAINER LAN-slide

USER root
RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /cs2/

RUN rm /cs2/config_match.py && rm /cs2/config_admins.py

ENV PYTHONUNBUFFERED=0
RUN chmod +x entrypoint.py

ENTRYPOINT ["./entrypoint.py"]
