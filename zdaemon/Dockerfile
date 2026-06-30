FROM base
LABEL maintainer="LAN-slide"

RUN dpkg --add-architecture i386 &&  apt-get update && apt-get install -y libc6-i386 libstdc++6:i386

RUN useradd -lm doom

ADD zserv*linux26.tgz /
RUN mkdir /zdaemon && mv /zserv*/* /zdaemon/ && chmod +x /zdaemon/zserv
WORKDIR /zdaemon

ADD wads/* /zdaemon/
ADD start-* ffa-template.cfg /zdaemon/

RUN chown doom /zdaemon -R
RUN chmod +x /zdaemon/start-ffa.sh 

CMD ["/zdaemon/start-ffa.sh"]

