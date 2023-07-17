FROM base
MAINTAINER LAN-slide

RUN useradd steam && mkdir /retrocycles /home/steam && chown steam:steam /retrocycles /home/steam -R

USER steam

COPY --chown=steam:steam data /retrocycles

WORKDIR /retrocycles

COPY --chown=steam:steam autoexec.cfg usr/etc/games/Retrocycles-dedicated/autoexec.cfg
COPY --chown=steam:steam server_info.cfg usr/etc/games/Retrocycles-dedicated/server_info.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT /retrocycles/entrypoint.sh
