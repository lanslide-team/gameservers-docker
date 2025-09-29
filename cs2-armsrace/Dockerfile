FROM cs2-base
LABEL maintainer="LAN-slide"

USER root
RUN mkdir -p /game/csgo/replays && chown -R steam:steam  /game/csgo/replays && chmod a+rwX /game/csgo/replays

USER steam
WORKDIR /cs2

COPY --chown=steam:steam defaultenv.ini stats.py /cs2/

ENTRYPOINT ["./entrypoint.py", "armsrace"]
