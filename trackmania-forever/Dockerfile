FROM base:latest
LABEL maintainer="LAN-slide"

## Put Trackmania Server zip file in this directory
## Download from http://files2.trackmaniaforever.com/TrackmaniaServer_2011-02-21.zip

RUN apt-get update && apt-get install -y apache2 php php-zip php-xml
RUN adduser tm && mkdir -p /tm && mkdir -p /var/log/apache2 && mkdir -p /var/run/apache2

WORKDIR /tm
ADD *.zip /tm/
RUN ls /tm/

RUN unzip /tm/TrackmaniaServer*.zip && unzip /tm/AdminServ*.zip
RUN mv /tm/AdminServ-master/* /var/www/html/ && rm /tm/AdminServ-master/ -rf
RUN mkdir /var/www/html/logs && chown www-data:www-data /var/www/html -R
RUN rm -f /tm/*.zip && rm -f /var/www/html/index.html
RUN chown tm:tm /tm /var/log/apache2 /var/run/apache2 -R
RUN chmod 777 /var/www/html/logs -R
RUN chmod 666 /var/www/html/config/adminlevel.cfg.php
RUN chmod 666 /var/www/html/config/adminserv.cfg.php
RUN chmod 666 /var/www/html/config/servers.cfg.php

ADD tracklist*.cfg /tm/GameData/Tracks/
ADD dedicated_cfg.txt /tm/GameData/Config/
ADD start_server.sh /tm/

CMD ["/tm/start_server.sh"]
