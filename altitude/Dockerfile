FROM ich777/debian-baseimage

LABEL org.opencontainers.image.authors="team@lanslide.com.au"
LABEL org.opencontainers.image.source="https://github.com/ich777/docker-altitude"

RUN dpkg --add-architecture i386 && \
	apt-get update && \
	export TZ=Melbourne/Victoria && \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
	apt-get -y install --no-install-recommends libc6:i386 bzip2 && \
	rm -rf /var/lib/apt/lists/*

ENV SERVER_DIR="/altitude"
ENV GAME_PARAMS=""
ENV UMASK=000
ENV UID=1000
ENV GID=1000
ENV DATA_PERM=770
ENV USER="altitude"

RUN mkdir $SERVER_DIR && \
	useradd -d $SERVER_DIR -s /bin/bash $USER && \
	chown -R $USER $SERVER_DIR && \
	ulimit -n 2048

ADD /scripts/ /opt/scripts/
RUN chmod +x /opt/scripts/start.sh
RUN chmod +x /opt/scripts/start-server.sh
RUN chown $USER /opt/scripts/ -R

USER $USER

#Server Start
ENTRYPOINT ["/opt/scripts/start.sh"]
