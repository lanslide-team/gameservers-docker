FROM base
MAINTAINER LAN-slide

RUN useradd -m steam && mkdir /csgo && chown steam:steam /csgo
    
USER steam

COPY --chown=steam:steam data /csgo

RUN rm /csgo/bin/libgcc_s.so.1 -f

RUN mkdir -p /csgo/csgo/resource/flash/econ/tournaments/teams/
