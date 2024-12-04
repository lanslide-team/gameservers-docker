FROM l4d2-base

MAINTAINER LAN-slide

USER steam
WORKDIR /l4d2

COPY --chown=steam:steam entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh
