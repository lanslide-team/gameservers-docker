FROM base

## Put Trackmania Server zip file in this directory
## Download from http://files2.trackmaniaforever.com/TrackmaniaServer_2011-02-21.zip

RUN apt-get install -y apache2 php php-zip php-xml
RUN adduser tm && mkdir /tm && chown tm:tm /tm

WORKDIR /tm
ADD *.zip /tm/
RUN ls /tm/

RUN unzip /tm/TrackmaniaServer*.zip && unzip /tm/AdminServ*.zip
RUN mv /tm/AdminServ-master/* /var/www/html/ && rm /tm/AdminServ-master/ -rf
RUN mkdir /var/www/html/logs && chown www-data:www-data /var/www/html -R
RUN rm -f /tm/*.zip && rm -f /var/www/html/index.html

ADD tracklist*.cfg /tm/GameData/Tracks/
ADD dedicated_cfg.txt /tm/GameData/Config/
Add start_server.sh /tm/

CMD ["/tm/start_server.sh"]
