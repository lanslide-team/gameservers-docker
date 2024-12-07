FROM l4d2-base

MAINTAINER LAN-slide

WORKDIR /l4d2/left4dead2/

RUN wget -nc "https://www.sourcemod.net/vbcompiler.php?file_id=75319" -O addons/sourcemod/plugins/l4dabt.smx
# Super Versus
#RUN wget -nc "https://www.sourcemod.net/vbcompiler.php?file_id=54755" -O addons/sourcemod/plugins/l4d_superversus.smx
#RUN wget -nc "https://forums.alliedmods.net/attachment.php?attachmentid=195032&d=1652367032" -O addons/sourcemod/plugins/l4d_superversus_latest.smx
RUN wget -nc "https://forums.alliedmods.net/attachment.php?attachmentid=181867&d=1591326080" -O addons/sourcemod/plugins/l4dunreservelobby.smx
RUN wget -nc "https://www.sourcemod.net/vbcompiler.php?file_id=183138" -O addons/sourcemod/plugins/l4d_superversus.smx

# DownTown Mod
#RUN wget -nc "https://forums.alliedmods.net/attachment.php?attachmentid=135418&d=1404865614" -O "left4downtown2-0.5.4.2.zip" && \
#    unzip left4downtown2-0.5.4.2.zip -d "addons/sourcemod/" && \
#    rm left4downtown2-0.5.4.2.zip -rf

# Using Left 4 DHooks Direction
RUN wget -nc "https://forums.alliedmods.net/attachment.php?attachmentid=195507&d=1730824361" -O "left4dhooks.zip" && \
    unzip "left4dhooks.zip" -d "addons/" && \
    rm "left4dhooks.zip" -f

# L4D toolz
RUN wget -nc "https://forums.alliedmods.net/attachment.php?attachmentid=122230&d=1373147952" -O "l4dtoolz(L4D2)-1.0.0.9h.zip" && \
    unzip "l4dtoolz(L4D2)-1.0.0.9h.zip" -d "addons/" && \
    rm "l4dtoolz(L4D2)-1.0.0.9h.zip" -f

# Tanks
RUN wget -nc "https://forums.alliedmods.net/attachment.php?attachmentid=193810&d=1645464100" -O "TankOnSpawn.zip" && \
    unzip "TankOnSpawn.zip" -d "addons/sourcemod/" && \
    rm "ankOnSpawn.zip" -f

#RUN chown steam:steam /l4d2 -R

#USER steam
WORKDIR /l4d2

COPY --chown=steam:steam cfg ./left4dead2/cfg
COPY --chown=steam:steam entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh
