FROM base
LABEL maintainer="LAN-slide"

RUN useradd -lm steam && mkdir /cs && chown steam:steam /cs
RUN mkdir /root/steam

RUN mkdir -p /home/steam/.steam/sdk32

WORKDIR /cs
COPY --chown=steam:steam data ./
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk32/steamclient.so
