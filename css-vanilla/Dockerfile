FROM css-base
MAINTAINER LAN-slide

USER steam
WORKDIR /css

COPY --chown=steam:steam entrypoint.py /css/

RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
