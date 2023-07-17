FROM sourcemod as sourcemod

FROM csgo-base
MAINTAINER LAN-slide

USER root
RUN apt-get install -y wget mysql-client

USER steam
WORKDIR /csgo

COPY --from=sourcemod --chown=steam:steam /csgo csgo
COPY databases.cfg csgo/addons/sourcemod/configs/

# Install smlib
RUN wget "https://github.com/bcserv/smlib/archive/refs/heads/transitional_syntax.zip" -O smlib.zip
RUN unzip smlib.zip && find smlib-transitional_syntax/* -maxdepth 0 -type f -delete && cp smlib-transitional_syntax/* csgo/addons/sourcemod/ -R && rm smlib.zip && rm smlib-transitional_syntax/ -rf

# Install multicolors
RUN wget "https://github.com/Bara/Multi-Colors/archive/refs/heads/master.zip" -O multicolors.zip
RUN unzip multicolors.zip && find Multi-Colors-master/* -maxdepth 0 -type f -delete && cp Multi-Colors-master/* csgo/ -R && rm multicolors.zip && rm Multi-Colors-master/ -rf

# Install colorlib
RUN wget "https://github.com/c0rp3n/colorlib-sm/archive/refs/heads/master.zip" -O colorlib.zip
RUN unzip colorlib.zip && find colorlib-sm-master/* -maxdepth 0 -type f -delete && cp colorlib-sm-master/* csgo/ -R && rm colorlib.zip && rm colorlib-sm-master/ -rf

# Install AutoExecConfig
RUN wget "https://github.com/Impact123/AutoExecConfig/archive/refs/heads/development.zip" -O auto_exec_config.zip
RUN unzip auto_exec_config.zip && cp AutoExecConfig-development/autoexecconfig.inc csgo/addons/sourcemod/scripting/include/ -R && cp AutoExecConfig-development/autoexecconfig.sp csgo/addons/sourcemod/scripting/ -R && rm auto_exec_config.zip && rm AutoExecConfig-development/ -rf

# Install End-Touch-Fix
RUN wget "https://github.com/rumourA/End-Touch-Fix/archive/refs/heads/master.zip" -O etf.zip
RUN unzip etf.zip && cp End-Touch-Fix-master/* csgo/addons/sourcemod -R && rm etf.zip && rm End-Touch-Fix-master/ -rf

# Install Stripper:Source
RUN wget "https://www.bailopan.net/stripper/snapshots/1.2/stripper-1.2.2-git141-linux.tar.gz" -O stripper.tar.gz && tar zvxf stripper.tar.gz -C csgo/ && rm stripper.tar.gz -f

# Install SurfTimer
RUN wget "https://github.com/surftimer/SurfTimer/archive/refs/heads/dev.zip" -O surftimer.zip
RUN unzip surftimer.zip && find SurfTimer-dev/* -maxdepth 0 -type f -delete && cp SurfTimer-dev/* csgo/ -R && rm surftimer.zip -f && rm SurfTimer-dev/ -rf

# Movement Unlocker
RUN wget "https://forums.alliedmods.net/attachment.php?attachmentid=141520&d=1421117043" -O csgo/addons/sourcemod/scripting/csgo_movement_unlocker.sp
RUN wget "https://forums.alliedmods.net/attachment.php?attachmentid=141521&d=1495261818" -O csgo/addons/sourcemod/gamedata/csgo_movement_unlocker.games.txt

# Install MomSurfFix
#RUN wget "https://github.com/GAMMACASE/MomSurfFix/archive/refs/heads/master.zip" -O mom.zip
#RUN unzip mom.zip && find MomSurfFix-master/* -maxdepth 0 -type f -delete && cp MomSurfFix-master/* csgo/ -R && rm mom.zip && rm MomSurfFix-master/ -rf

# Install rngfix
RUN wget "https://github.com/jason-e/rngfix/archive/refs/heads/master.zip" -O rngfix.zip
RUN unzip rngfix.zip && find rngfix-master/* -maxdepth 0 -type f -delete && cp rngfix-master/plugin/* csgo/addons/sourcemod -R && rm rngfix.zip && rm rngfix-master/ -rf

# Install HeadBugFix
RUN wget "https://github.com/GAMMACASE/HeadBugFix/archive/refs/heads/master.zip" -O headbugfix.zip
RUN unzip headbugfix.zip && find HeadBugFix-master/* -maxdepth 0 -type f -delete && cp HeadBugFix-master/* csgo/ -R && rm headbugfix.zip && rm HeadBugFix-master/ -rf

# Install PushFixDE
#RUN wget "https://github.com/GAMMACASE/PushFixDE/archive/refs/heads/master.zip" -O pushfix.zip
#RUN unzip pushfix.zip && find PushFixDE-master/* -maxdepth 0 -type f -delete && cp PushFixDE-master/* csgo/ -R && rm pushfix.zip && rm PushFixDE-master/ -rf

# Install crouchboostfix
# RUN wget "https://github.com/t5mat/crouchboostfix/blob/master/crouchboostfix.sp" -O csgo/addons/sourcemod/scripting/crouchboostfix.sp

# Install Normalized-Run-Speed
RUN wget "https://github.com/sneak-it/Normalized-Run-Speed/archive/refs/heads/master.zip" -O run_speed.zip
RUN unzip run_speed.zip && find Normalized-Run-Speed-master/* -maxdepth 0 -type f -delete && cp Normalized-Run-Speed-master/* csgo/addons/sourcemod -R && rm run_speed.zip && rm Normalized-Run-Speed-master/ -rf

# Install Dynamic DHooks (dtour)
RUN wget "https://forums.alliedmods.net/attachment.php?attachmentid=190123&d=1625050030" -O dhooks.zip
RUN unzip dhooks.zip -d dhooks && cp dhooks/addons/sourcemod/scripting/include/dhooks.inc csgo/addons/sourcemod/scripting/include/ -f && rm dhooks.zip -f && rm dhooks/ -rf

# Initialise DB
RUN MYSQL_ROOT_PASSWORD=`echo -n l33t | sha256sum | base64 | head -c 32 ; echo` && \
    sed -i "s/\${MYSQL_ROOT_PASSWORD}/$MYSQL_ROOT_PASSWORD/" csgo/addons/sourcemod/configs/databases.cfg

# Compile plugins
RUN csgo/addons/sourcemod/scripting/compile.sh && cp csgo/addons/sourcemod/scripting/compiled/* csgo/addons/sourcemod/plugins

# Compile surf config and maps
COPY --chown=steam:steam cfg csgo/cfg
COPY --chown=steam:steam maps csgo/maps
COPY --chown=steam:steam mapcycle.txt csgo/

COPY --chown=steam:steam entrypoint.py defaultenv.ini stats.py ./

ENV PYTHONUNBUFFERED=0

ENTRYPOINT ["./entrypoint.py"]
