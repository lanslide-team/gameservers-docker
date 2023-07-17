FROM sourcemod as sourcemod

FROM csgo-base
MAINTAINER LAN-slide

USER steam
WORKDIR /csgo

# Get sourcemod files
COPY --from=sourcemod --chown=steam:steam /csgo /csgo/csgo

RUN cd /csgo/csgo/addons/sourcemod/plugins/ && \
    mv *.smx disabled/ && \
    cd disabled && \
    mv admin-flatfile.smx basecommands.smx .. && \
    cd .. && rm -rf disabled

RUN cd /csgo/csgo/addons/sourcemod && \
    curl -L https://github.com/Maxximou5/csgo-deathmatch/archive/refs/heads/master.zip > deathmatch.zip && \
    unzip deathmatch.zip && \
    cp csgo-deathmatch-master/* . -R && \
    rm csgo-deathmatch-master -rf &&  \
    rm deathmatch.zip

#RUN cd /csgo/addons/sourcemod/plugins/ && rm admin-sql-prefetch.smx \
#        basetriggers.smx \
#        playercommands.smx \
#        admin-sql-threaded.smx \
#        basevotes.smx \
#        randomcycle.smx \
#        adminhelp.smx \
#        clientprefs.smx \
#        reservedslots.smx \
#        adminmenu.smx \
#        funcommands.smx \
#        rockthevote.smx \
#        antiflood.smx \
#        funvotes.smx \
#        sounds.smx \
#        basebans.smx \
#        mapchooser.smx \
#        sql-admin-manager.smx \
#        basechat.smx \
#        nextmap.smx \
#        basecomm.smx \
#        nominations.smx

COPY --chown=steam:steam de_dust2.txt /csgo/csgo/addons/sourcemod/configs/deathmatch/spawns/
COPY --chown=steam:steam cfg /csgo/cfg
COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py /csgo/

ENTRYPOINT ["./entrypoint.py"]
