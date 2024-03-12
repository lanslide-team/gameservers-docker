FROM base

RUN apt-get update && apt-get install -y curl

RUN mkdir /css

COPY config_admins.py /
COPY config_match.py /

RUN curl -s https://mms.alliedmods.net/mmsdrop/2.0/mmsource-2.0.0-git1281-linux.tar.gz | tar zxf - -C /css

RUN wget $(wget -q -O - https://api.github.com/repos/shobhit-pathak/MatchZy/releases/latest | jq -r '.assets[] | select(.name | contains ("with-cssharp")) | .browser_download_url') -O matchzy.zip && unzip matchzy.zip -d /css && rm matchzy.zip -f

#RUN css_latest=$(curl -s "https://api.github.com/repos/roflmuffin/CounterStrikeSharp/releases/latest" | grep -E "runtime.*linux.*zip" | cut -d : -f 2,3 | tr -d \" | sed -n '2p') && wget -nc ${css_latest} -O css.zip && unzip css.zip -d /css && rm css.zip -f

#COPY addons /css/addons
#COPY cfg /css/cfg
COPY Lanslide /css/addons/counterstrikesharp/plugins/Lanslide
COPY MatchZy /css/addons/counterstrikesharp/plugins/MatchZy
