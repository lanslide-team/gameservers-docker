FROM base

RUN apt-get update && apt-get install -y git \
#    libc6:i386 \
    libc6-dev-i386 \
    lib32stdc++6

  #  build-essential \
  #  libstdc++6
#lib32gcc1 \
#lib32stdc++6

RUN git clone https://gitlab+deploy-token-190229:ADidL2yx3YB-RmvuCxNC@gitlab.com/lanslide/ls-sourcemod.git
RUN cd ls-sourcemod/ && ./ncompile.sh
