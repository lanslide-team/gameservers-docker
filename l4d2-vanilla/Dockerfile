FROM l4d2-base

LABEL maintainer="LAN-slide"

USER steam
WORKDIR /l4d2

COPY --chown=steam:steam entrypoint.sh ./entrypoint.sh
COPY --chown=steam:steam cfg ./left4dead2/cfg

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh
