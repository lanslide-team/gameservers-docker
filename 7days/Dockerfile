FROM almalinux:latest
MAINTAINER LAN-slide

RUN useradd steam && mkdir /7days && chown steam:steam /7days

RUN yum update -y && yum install -y epel-release

RUN yum install -y \
    glibc.i686 \
    libstdc++.i686 \
    zlib.i686 \
    python39 \
    python39-pip

RUN pip3.9 install asyncio opengsq

USER steam

COPY --chown=steam:steam data /7days

WORKDIR /7days

COPY --chown=steam:steam entrypoint.sh entrypoint.sh
COPY --chown=steam:steam serverconfig.xml serverconfig.xml
COPY --chown=steam:steam stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT /7days/entrypoint.sh
