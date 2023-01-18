FROM itzg/minecraft-server

RUN apt -y update
RUN apt install  -y iproute2 python3.9 python3-pip
RUN python3.9 -m pip install asyncio opengsq

RUN git clone https://github.com/Tiiffi/mcrcon.git /tmp/mcrcon
RUN cd /tmp/mcrcon && make && make install && rm /tmp/mcrcon -rf

COPY advertise.py /advertise.py
COPY entrypoint.sh /entrypoint.sh
COPY stats.py /data/stats.py

USER root
RUN chmod +x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
