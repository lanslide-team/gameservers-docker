FROM cs-base
LABEL maintainer="LAN-slide"

RUN apt-get update && apt-get install -y gdb

USER steam
WORKDIR /cs

COPY --chown=steam:steam entrypoint.py /cs/

RUN chmod +x entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
