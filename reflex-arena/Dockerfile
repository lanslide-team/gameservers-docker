# This may use wine or wine-src
FROM wine

#RUN useradd -m steam && mkdir /reflex-arena && chown steam:steam /reflex-arena
RUN mkdir /reflex-arena
WORKDIR /reflex-arena

COPY data ./
COPY entrypoint.sh ./ 

RUN chmod +x /reflex-arena/entrypoint.sh

CMD ["/reflex-arena/entrypoint.sh"]
