# This may use wine or wine-src
FROM wine
LABEL maintainer="LAN-slide"

#RUN useradd -m steam && mkdir /reflex-arena && chown steam:steam /reflex-arena
RUN mkdir /reflex-arena
WORKDIR /reflex-arena

COPY data ./
COPY entrypoint.sh ./ 

RUN useradd -lm reflex && chown reflex /reflex-arena -R

RUN chmod +x /reflex-arena/entrypoint.sh

CMD ["/reflex-arena/entrypoint.sh"]
