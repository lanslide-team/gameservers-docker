FROM wineconsole/lite

WORKDIR /haloce
COPY data /haloce
COPY entrypoint.sh /entrypoint.sh
COPY init.txt /haloce

RUN wget -nc "http://www.lanslide.com.au/storage/haloce/maps.zip" -O maps.zip && \
    unzip -o maps.zip  && \
    rm maps.zip -f

RUN chmod +x /entrypoint.sh

EXPOSE 2302/udp 2303/udp

CMD "/entrypoint.sh"

