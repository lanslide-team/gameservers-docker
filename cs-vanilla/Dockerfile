FROM cs-base
LABEL maintainer="LAN-slide"

USER steam
WORKDIR /cs

COPY --chown=steam:steam entrypoint.py /cs/

RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
