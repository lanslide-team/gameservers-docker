FROM wineconsole/lite
LABEL maintainer="LAN-slide"

RUN apk add --no-cache wget unzip su-exec

RUN adduser -D -h /haloce halo \
 && mkdir -p /haloce/.wine \
 && chown -R halo:halo /haloce

WORKDIR /haloce
COPY data /haloce
COPY init.txt /haloce
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN wget -nc "http://www.lanslide.com.au/storage/haloce/maps.zip" -O maps.zip \
 && unzip -o maps.zip \
 && rm -f maps.zip \
 && chown -R halo:halo /haloce

ENV HOME=/haloce
ENV WINEPREFIX=/haloce/.wine

EXPOSE 2302/udp 2303/udp

CMD ["/entrypoint.sh"]

