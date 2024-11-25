FROM base
MAINTAINER LAN-slide

RUN useradd -lm steam && mkdir /css && chown steam:steam /css
RUN mkdir /root/steam

WORKDIR /css
COPY --chown=steam:steam data ./
