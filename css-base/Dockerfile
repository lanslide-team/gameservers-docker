FROM base
LABEL maintainer="LAN-slide"

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y \
        libncurses5:i386 \
        libtinfo5:i386

RUN useradd -lm steam && mkdir /css && chown steam:steam /css
RUN mkdir -p /root/steam
RUN mkdir -p /home/steam/.steam/sdk32

WORKDIR /css
COPY --chown=steam:steam data ./
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk32/steamclient.so

