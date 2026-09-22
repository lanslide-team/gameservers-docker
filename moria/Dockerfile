FROM golang:1.26.0-trixie AS tools-builder

COPY patcher patcher
RUN go build -C patcher
COPY healthcheck healthcheck
RUN go build -C healthcheck

FROM wine
LABEL maintainer="LAN-slide"

USER root

RUN mkdir -p /tmp/.X11-unix \
    && chown root:root /tmp/.X11-unix \
    && chmod 1777 /tmp/.X11-unix

WORKDIR /moria

ENV WINEPREFIX=/wineprefix-template

COPY --chown=ls:ls entrypoint.sh data config ./
COPY --chown=ls:ls mods ./mods
RUN chown ls:ls /moria

COPY --from=tools-builder /go/patcher/patcher /usr/local/bin/patcher
COPY --from=tools-builder /go/healthcheck/healthcheck /usr/local/bin/healthcheck

RUN chmod +x entrypoint.sh && chmod +x /usr/local/bin/patcher && chmod +x /usr/local/bin/healthcheck
HEALTHCHECK --interval=1m --timeout=10s --start-period=5m --start-interval=15s --retries=2 CMD healthcheck localhost:7777

USER ls

CMD ["./entrypoint.sh"]

