FROM base
LABEL maintainer="LAN-slide"

RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y libstdc++6:i386 p7zip-full && apt-get clean

COPY dedicatedserver*.7z /

RUN 7z x /dedicatedserver*.7z && rm /dedicatedserver*.7z
RUN mv /dedicatedserver* /ut2004

RUN useradd ut && chown ut /ut2004 -R

USER ut

WORKDIR /ut2004
COPY entrypoint.sh /ut2004/entrypoint.sh

RUN sed -i 's/\r$//' /ut2004/entrypoint.sh \
 && chmod +x /ut2004/entrypoint.sh \
 && chmod +x /ut2004/System/ucc*

ENTRYPOINT ["/ut2004/entrypoint.sh"]
