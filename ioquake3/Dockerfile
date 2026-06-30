FROM base
LABEL maintainer="LAN-slide"

RUN useradd ioquake3 && mkdir /home/ioquake3 && chown ioquake3 /home/ioquake3 /home/
RUN apt-get update && apt-get install -y git cmake-data dh-elpa-helper emacsen-common libarchive13 libjsoncpp25 librhash0 libuv1

RUN wget -q https://github.com/Kitware/CMake/releases/download/v4.1.1/cmake-4.1.1-linux-x86_64.sh && \
    chmod +x cmake-4.1.1-linux-x86_64.sh && \
    ./cmake-4.1.1-linux-x86_64.sh --skip-license --prefix=/usr/local && \
    rm cmake-4.1.1-linux-x86_64.sh

USER ioquake3

WORKDIR /home/
ENV COPYDIR=/home/ioquake3

# RUN git clone https://github.com/nrempel/q3-server.git

RUN wget https://raw.githubusercontent.com/ioquake/ioq3/master/misc/linux/server_compile.sh

RUN chmod +x server_compile.sh

RUN sh -c 'yes | ./server_compile.sh' && rm -f server_compile.sh
RUN mv /home/ioquake3/ioquake3/* /home/ioquake3 && rm /home/ioquake3/ioquake3 -rf

WORKDIR /home/ioquake3/

RUN wget https://files.ioquake3.org/quake3-latest-pk3s.zip && unzip quake3-latest-pk3s.zip

RUN cp ./quake3-latest-pk3s/* . -r && rm -rf ./quake3-latest-pk3s/ quake3-latest-pk3s.zip

RUN wget -P baseq3 https://github.com/nrempel/q3-server/raw/master/baseq3/pak0.pk3

COPY --chown=ioquake3:ioquake3 baseq3/server.cfg baseq3/server.cfg
COPY --chown=ioquake3:ioquake3 entrypoint.sh entrypoint.sh
COPY --chown=ioquake3:ioquake3 stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/home/ioquake3/entrypoint.sh"]
