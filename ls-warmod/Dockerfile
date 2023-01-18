FROM almalinux:latest

RUN yum update -y

RUN yum install -y git \
    glibc.i686 \
    libstdc++.i686

RUN git clone https://gitlab+deploy-token-190229:ADidL2yx3YB-RmvuCxNC@gitlab.com/lanslide/ls-sourcemod.git && cd ls-sourcemod/ && bash ncompile.sh
