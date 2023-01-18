FROM almalinux:latest
MAINTAINER LAN-slide

RUN useradd steam && mkdir /retrocycles && chown steam:steam /retrocycles

RUN yum update -y && yum install -y epel-release

USER steam

COPY --chown=steam:steam data /retrocycles

WORKDIR /retrocycles

COPY --chown=steam:steam autoexec.cfg usr/etc/games/Retrocycles-dedicated/autoexec.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT /retrocycles/entrypoint.sh
