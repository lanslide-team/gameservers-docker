FROM factoriotools/factorio:latest

ARG PUID=1000
ARG PGID=1000

USER root

RUN groupmod -g ${PGID} factorio || true && \
    usermod -u ${PUID} -g ${PGID} factorio || true && \
    chown -R ${PUID}:${PGID} /factorio && \
    chown -R ${PUID}:${PGID} /opt/factorio || true

USER ${PUID}:${PGID}
WORKDIR /factorio
