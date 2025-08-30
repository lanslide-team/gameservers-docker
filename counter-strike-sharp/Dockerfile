FROM base

RUN apt-get update && apt-get install -y curl dotnet-sdk-8.0

RUN mkdir /css

COPY config_admins.py /
COPY config_match.py /
COPY config_whitelist.py /

RUN mm_minor_version=$(curl -s https://mms.alliedmods.net/mmsdrop/ | grep -Eo "\"2\.[0-9]*" -o | cut -c 4- | sort -rn | head -n 1) && \
    mm_latest=$(curl -s https://mms.alliedmods.net/mmsdrop/2.${mm_minor_version}/mmsource-latest-linux) && \
    curl -s https://mms.alliedmods.net/mmsdrop/2.${mm_minor_version}/${mm_latest} | tar zxf - -C /css


###########$##i######################## COUNTERSTRIKESHARP ##########################################

RUN set -eux; \
    URL=$(curl -s https://api.github.com/repos/roflmuffin/CounterStrikeSharp/releases/latest \
        | grep "browser_download_url.*with-runtime-linux" \
        | cut -d '"' -f 4); \
    curl -L "$URL" -o cssharp.zip; \
    unzip -o cssharp.zip -d /css; \
    rm cssharp.zip

#############i############################$## PUGSHARP ##############################################


#RUN URL="$(curl -fsSL "https://api.github.com/repos/Lan2Play/PugSharp/releases?per_page=1" \
#      | jq -r '.[0].assets[] | select(.name | test("PugSharp_linux.*\\.zip$")) | .browser_download_url' \
#      | head -n1 || true)"; \
#    curl -fL "$URL" -o /tmp/pugsharp.zip; \
#    unzip -o /tmp/pugsharp.zip -d /css; \
#    rm -f /tmp/pugsharp.zip
    
#############i################################ MATCHZY ##############################################
RUN git clone https://github.com/shobhit-pathak/MatchZy /tmp/MatchZy && \ 
    cd /tmp/MatchZy && \
    git config --global user.name "LAN-slide" && \
    git config --global user.email "team@lanslide.com.au" && \
    git fetch origin pull/228/head:pr-228 && \
    git checkout main && \
    git merge --no-ff pr-228 -m "Merging PR into main" && \
    dotnet publish

RUN mkdir -p /css/cfg/MatchZy && cp /tmp/MatchZy/cfg/MatchZy /css/cfg/MatchZy -R
RUN cp /tmp/MatchZy/bin/Release/net8.0/publish /css/addons/counterstrikesharp/plugins/MatchZy -R

# ARG version="0.8.12"
# ARG matchzy="https://github.com/shobhit-pathak/MatchZy/releases/download/${version}/MatchZy-${version}-with-cssharp-linux.zip"
# RUN wget -nc ${matchzy} -O m.zip && unzip m.zip -d /css && rm m.zip -f
#####################################################################################################

#COPY addons /css/addons`
#COPY cfg /css/cfg
#COPY Lanslide /css/addons/counterstrikesharp/plugins/Lanslide
#COPY MatchZy /css/addons/counterstrikesharp/plugins/MatchZy
