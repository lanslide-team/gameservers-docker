FROM base

RUN apt-get update && apt-get install -y curl

RUN mkdir /cs2

# Install Metamod + Sourcemod
RUN mm_minor_version=$(curl -s https://mms.alliedmods.net/mmsdrop/ | grep -Eo "1\.[0-9]*" -o | cut -c 3- | sort -rn | head -n 1) && \
    mm_latest=$(curl -s https://mms.alliedmods.net/mmsdrop/1.${mm_minor_version}/mmsource-latest-linux) && \
    curl -s https://mms.alliedmods.net/mmsdrop/1.${mm_minor_version}/${mm_latest} | tar zxf - -C /cs2
   
# Use 2p for stable release
RUN sm_minor_version=$(curl -s https://sm.alliedmods.net/smdrop/ | grep -Eo "\"1\.[0-9]*" -o | cut -c 4- | sort -rn | sed -n '1p') && \
    sm_latest=$(curl -s https://sm.alliedmods.net/smdrop/1.${sm_minor_version}/sourcemod-latest-linux) && \
    curl -s https://sm.alliedmods.net/smdrop/1.${sm_minor_version}/${sm_latest} | tar zxf - -C /cs2

ADD admins_simple.ini /csgo/addons/sourcemod/configs/

RUN cd /csgo/addons/sourcemod/plugins && rm -fv funcommands.smx funvotes.smx nextmap.smx
