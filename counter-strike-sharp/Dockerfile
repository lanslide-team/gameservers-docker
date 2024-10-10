FROM base

RUN apt-get update && apt-get install -y curl

RUN mkdir /css

COPY config_admins.py /
COPY config_match.py /

RUN curl -s https://mms.alliedmods.net/mmsdrop/2.0/mmsource-2.0.0-git1314-linux.tar.gz | tar zxf - -C /css 

#RUN wget -nc "https://github.com/Lan2Play/PugSharp/releases/download/v0.1.7-beta/PugSharp_with_cssharp_and_runtime_linux_0.1.7-beta.zip" -O matchzy.zip && unzip matchzy.zip -d /css && rm matchzy.zip -f

#RUN css_latest=$(curl -s "https://api.github.com/repos/roflmuffin/CounterStrikeSharp/releases/latest" | grep -E "runtime.*linux.*zip" | cut -d : -f 2,3 | tr -d \" | sed -n '2p')
#RUN wget -nc ${css_latest} -O css.zip && unzip css.zip -d /css && rm css.zip -f

#RUN matchzy=$(curl -s "https://api.github.com/repos/shobhit-pathak/MatchZy/releases/latest" | grep -E "with-cssharp-linux.*zip" | cut -d : -f 2,3 | tr -d \" | sed -n '2p' | xargs)
ARG version="0.8.5"
ARG matchzy="https://github.com/shobhit-pathak/MatchZy/releases/download/${version}/MatchZy-${version}-with-cssharp-linux.zip"
RUN wget -nc ${matchzy} -O m.zip && unzip m.zip -d /css && rm m.zip -f

#COPY addons /css/addons`
#COPY cfg /css/cfg
COPY Lanslide /css/addons/counterstrikesharp/plugins/Lanslide
COPY MatchZy /css/addons/counterstrikesharp/plugins/MatchZy
