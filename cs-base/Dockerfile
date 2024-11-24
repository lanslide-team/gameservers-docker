FROM base
MAINTAINER LAN-slide

RUN useradd -lm steam && mkdir /cs && chown steam:steam /cs
RUN mkdir /root/steam

WORKDIR /cs
COPY --chown=steam:steam data ./
