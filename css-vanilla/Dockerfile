FROM css-base
LABEL maintainer="LAN-slide"

USER steam
WORKDIR /css

COPY --chown=steam:steam entrypoint.py /css/

RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
