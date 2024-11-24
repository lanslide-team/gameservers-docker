FROM cs-base
MAINTAINER LAN-slide

USER steam
WORKDIR /cs

COPY --chown=steam:steam entrypoint.py /cs/

RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
