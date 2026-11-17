ARG IMAGE_VERSION=preview
FROM sdvd/server:${IMAGE_VERSION}

LABEL maintainer="LAN-slide"

USER 0:0

RUN apt-get update && apt-get install python3 unzip -y

# Copy pre-downloaded Stardew Valley game files
COPY data/ /data/game/
COPY steamclient.so /data/game/.steam-sdk/linux64/steamclient.so

RUN test -s /data/game/StardewValley && \
    test -s "/data/game/Stardew Valley.dll" && \
    test -d /data/game/Content && \
    chmod +x /data/game/StardewValley && \
    touch /data/game/.download-manifest-413150

COPY server-settings.json /defaults/server-settings.json
COPY configure-settings.py /usr/local/bin/configure-settings.py
COPY start-custom.sh /usr/local/bin/start-custom.sh

RUN chmod +x /data/game/StardewValley

# Ensure game files are accessible to UID/GID 1000
RUN chown -R 1000:1000 /data /tmp
RUN chmod +x /usr/local/bin/start-custom.sh

# Install mods
COPY mods/ /tmp/mods/
RUN mkdir -p /data/Mods/extra \
    && for zip in /tmp/mods/*.zip; do \
        [ -f "$zip" ] || continue; \
        unzip -q "$zip" -d /data/Mods/extra; \
    done \
    && rm -rf /tmp/mods

ENV USER_ID=1000 \
    GROUP_ID=1000 \
    HOME=/tmp \
    ALSOFT_DRIVERS=null \
    XAUTHORITY=/tmp/.Xauthority \
    VALIDATE_ON_BOOT=false

ENTRYPOINT ["/usr/local/bin/start-custom.sh"]
CMD []

