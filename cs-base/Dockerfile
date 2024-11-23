FROM base
MAINTAINER LAN-slide

RUN useradd -lm steam && mkdir /cs && chown steam:steam /cs

USER steam
WORKDIR /cs

COPY --chown=steam:steam entrypoint.py ./
COPY --chown=steam:steam data ./
#COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk64/steamclient.so

RUN chmod +x entrypoint.py

ENTRYPOINT ["./entrypoint.py"]
