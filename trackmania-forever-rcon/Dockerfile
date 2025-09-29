FROM base
RUN apt-get install -y nginx php8.1-common php8.1-cli php8.1-fpm php8.1-xml
LABEL maintainer="LAN-slide"

ADD RemoteControlExamples/PhpRemote/* /var/www/html/
ADD default.conf /etc/nginx/sites-available/default
ADD start.sh /start.sh
RUN mkdir /run/php # for phpfpm 

CMD ["/start.sh"]


