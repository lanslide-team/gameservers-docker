FROM almalinux:latest
MAINTAINER LAN-slide

RUN useradd steam && mkdir /csgo && chown steam:steam /csgo

RUN dnf update -y && dnf install -y epel-release

RUN dnf install -y \
    glibc.i686 \
    libstdc++.i686 \
    zlib.i686 \
    unzip \
    curl \ 
    python39 \
    python39-pip

RUN pip3.9 install asyncio opengsq rcon

USER steam

COPY --chown=steam:steam data /csgo

# RUN rm /csgo/bin/libgcc_s.so.1 -f

RUN mkdir -p /csgo/csgo/resource/flash/econ/tournaments/teams/
