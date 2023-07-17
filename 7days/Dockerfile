FROM base
MAINTAINER LAN-slide

RUN useradd -m steam && mkdir /7days && chown steam:steam /7days

USER steam

COPY --chown=steam:steam data /7days

WORKDIR /7days

COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam serverconfig.xml serverconfig.xml
COPY --chown=steam:steam stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT /7days/entrypoint.sh
