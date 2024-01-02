FROM base

RUN apt-get update && apt-get install -y curl

RUN mkdir /css

#RUN mm_latest=$(curl -s "https://www.sourcemm.net/downloads.php?branch=master" | grep -Eo "https.*linux.*.gz" | head -n 1) && \
#    curl -s ${mm_latest} | tar zxf - -C /css

RUN curl -s https://mms.alliedmods.net/mmsdrop/2.0/mmsource-2.0.0-git1275-linux.tar.gz | tar zxf - -C /css

#RUN css_latest=$(curl -s "https://api.github.com/repos/roflmuffin/CounterStrikeSharp/releases/latest" | grep -E "runtime.*linux.*zip" | cut -d : -f 2,3 | tr -d \" | sed -n '2p') && \
#    wget -nc ${css_latest} -O css.zip && unzip css.zip -d /css && rm css.zip -f

COPY addons /css/addons
COPY cfg /css/cfg
COPY Lanslide /css/addons/counterstrikesharp/plugins/Lanslide

#RUN unzip PugSharp_with_cssharp_and_runtime_linux_0.0.1-alpha.zip -d /css && rm *.zip -f
#&& rm PugSharp_with_cssharp_and_runtime_linux_*.zip -f
#&& rm /css/PugSharp_with_cssharp_and_runtime_linux_*.zip -f

#RUN pugsharp_latest=$(curl -s "https://api.github.com/repos/Lan2Play/PugSharp/releases" | grep -E "PugSharp_linux.*zip" | cut -d : -f 2,3 | tr -d \" | sed -n '2p') && \
#    wget -nc ${pugsharp_latest} -O pugsharp.zip && unzip pugsharp.zip -d /css && rm pugsharp.zip -f
