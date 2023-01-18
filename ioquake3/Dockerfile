FROM almalinux:latest
MAINTAINER LAN-slide

RUN useradd ioq3srv && mkdir /ioquake3 && chown ioq3srv:ioq3srv /ioquake3

RUN yum update -y && yum install -y epel-release
    
#glibc.i686 \
#    libstdc++.i686 \

RUN yum install -y \
    git \
    gcc \
    make \
    wget \ 
    unzip \
    python39 \
    python39-pip

RUN pip3.9 install asyncio opengsq

USER ioq3srv

WORKDIR /ioquake3

# RUN git clone https://github.com/nrempel/q3-server.git

RUN wget https://raw.githubusercontent.com/ioquake/ioq3/master/misc/linux/server_compile.sh

RUN chmod +x server_compile.sh

RUN sh -c 'yes | ./server_compile.sh' && chown ioq3srv:ioq3srv ~/ioquake3 -R

RUN wget https://files.ioquake3.org/quake3-latest-pk3s.zip && unzip quake3-latest-pk3s.zip

RUN cp /ioquake3/quake3-latest-pk3s/* ~/ioquake3/ -r

WORKDIR /home/ioq3srv/ioquake3

RUN wget -P baseq3 https://github.com/nrempel/q3-server/raw/master/baseq3/pak0.pk3

COPY --chown=ioq3srv:ioq3srv baseq3/server.cfg baseq3/server.cfg
COPY --chown=ioq3srv:ioq3srv entrypoint.sh entrypoint.sh
COPY --chown=ioq3srv:ioq3srv stats.py stats.py

RUN chmod +x entrypoint.sh

ENTRYPOINT /home/ioq3srv/ioquake3/entrypoint.sh
