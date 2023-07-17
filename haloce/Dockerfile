FROM wineconsole/lite

WORKDIR /haloce
COPY data /haloce
COPY entrypoint.sh /entrypoint.sh
COPY init.txt /haloce

RUN chmod +x /entrypoint.sh

EXPOSE 2302/udp 2303/udp

CMD "/entrypoint.sh"

