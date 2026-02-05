FROM base
LABEL maintainer="LAN-slide"

RUN useradd -m steam && mkdir /compat /wreckfest2 /wreckfest2/save /proton && chown steam:steam /compat /wreckfest2 /wreckfest2/save /proton

ENV WINEPREFIX=/compat
ENV STEAM_COMPAT_DATA_PATH=/compat

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
      ca-certificates \
      bash coreutils procps \
      lib32gcc-s1 lib32stdc++6 \
      libc6:i386 libstdc++6:i386 libgcc-s1:i386 \
      libncurses6:i386 libtinfo6:i386 zlib1g:i386 \
      libcurl4:i386 \
      libx11-6:i386 libxext6:i386 libxrender1:i386 libxi6:i386 libxrandr2:i386 \
      libgl1:i386 libgl1-mesa-dri:i386 \
      libvulkan1 libvulkan1:i386 \
    && rm -rf /var/lib/apt/lists/*

USER steam
WORKDIR /wreckfest2

COPY --chown=steam:steam data ./
COPY --chown=steam:steam default_loop.becl ./save/
COPY --chown=steam:steam proton /proton
COPY --chown=steam:steam entry.sh ./
COPY --chown=steam:steam server_config.scnf ./save/

RUN chmod +x entry.sh
ENTRYPOINT ./entry.sh

