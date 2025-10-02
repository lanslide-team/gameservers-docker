FROM base:latest AS jdk
LABEL maintainer="LAN-slide"
ARG spigot_version=latest
ENV SPIGOT_VERSION=1.21.9
ARG java_version=21
ENV JAVA_VERSION=${java_version}
# todo: collapse these to single command
RUN sed --in-place --regexp-extended "s/(\/\/)(archive\.ubuntu)/\1au.\2/" /etc/apt/sources.list \
    && apt-get install -y software-properties-common \ 
    && apt-add-repository ppa:openjdk-r/ppa && \
       apt-get update
RUN apt-get install -y ca-certificates-java
RUN echo "yes" | apt-get install -y openjdk-${JAVA_VERSION}-jdk
RUN adduser spigot && mkdir /spigot && chown spigot:spigot /spigot -R
WORKDIR /spigot

RUN git clone https://github.com/Tiiffi/mcrcon.git /tmp/mcrcon
RUN cd /tmp/mcrcon && make && make install && rm /tmp/mcrcon -rf

FROM jdk AS build
WORKDIR /build
RUN apt-get install git -y && chown spigot:spigot . -R
USER spigot
RUN wget -O BuildTools.jar \
    https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar && \
    java -jar BuildTools.jar --rev $SPIGOT_VERSION

##%%%%%%%%%%%%%%%%%%%################################# PLUGINS ##%%%%%%%%%%%%%%%%%%%#################################

# DYNMAP
RUN wget https://dynmap.us/builds/dynmap/Dynmap-HEAD-spigot.jar

# ESSENTIALS-X
RUN wget -O ess.zip https://ci.ender.zone/job/EssentialsX/lastSuccessfulBuild/artifact/jars/*zip*/jars.zip && \
    unzip ess.zip && rm ess.zip -f

# GEYSER
RUN wget -O Geyser-Spigot.jar https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot

# JOIN COMMANDS
RUN wget -O join.zip https://jenkins.sirblobman.xyz/job/SirBlobman/job/JoinCommands/job/main/lastSuccessfulBuild/artifact/*zip*/target.zip && \
    unzip join.zip && rm join.zip -f

# LUCKPERMS
RUN set -eux; \
    URL="$(curl -fsSL https://metadata.luckperms.net/data/downloads | jq -r ".downloads.bukkit")"; \
    curl -fsSL "$URL" -o LuckPerms-Bukkit.jar

# MULTI-VERSE-CORE
RUN wget -qO Multiverse-Core.jar \
    $(curl -s https://api.github.com/repos/Multiverse/Multiverse-Core/releases/latest | \
    grep "browser_download_url.*jar" | \
    cut -d '"' -f 4)

# PLOTSQUARED
RUN set -eux; \
    git clone --depth=1 https://github.com/IntellectualSites/PlotSquared.git /tmp/plotsquared && \
    cd /tmp/plotsquared && ./gradlew build && \
    cp /tmp/plotsquared/Bukkit/build/libs/plotsquared-bukkit-*-SNAPSHOT.jar /build/plotsquared-bukkit.jar && \
    cd /build

# PLOT2DYNMAP
RUN set -eux; \
    API_URL="https://api.modrinth.com/v2/project/plot2dynmap/version"; \
    LATEST_URL="$(curl -fsSL "$API_URL" | jq -r '.[0].files[0].url')"; \
    wget -O Plot2Dynmap.jar "$LATEST_URL"

# PROTOCOL
RUN wget -qO ProtocolLib.jar \
    $(curl -s https://api.github.com/repos/dmulloy2/ProtocolLib/releases/latest | \
    grep "browser_download_url.*jar" | \
    cut -d '"' -f 4)

# VAULT
RUN wget -qO Vault.jar \
    $(curl -s https://api.github.com/repos/MilkBowl/Vault/releases/latest | \
    grep "browser_download_url.*jar" | \
    cut -d '"' -f 4)

# WORLD BORDER
RUN wget -qO WorldBorder.jar \
    $(curl -s https://api.github.com/repos/PryPurity/WorldBorder/releases/latest | \
    grep "browser_download_url.*jar" | \
    cut -d '"' -f 4)

# WORLD EDIT
RUN set -uex; \
    URL=$(curl -fsSL "https://api.modrinth.com/v2/project/worldedit/version" | jq -r '.[0].files[0].url'); \
    wget -O WorldEdit.jar "$URL"

#####################################################################################################################

FROM jdk AS final
ADD server.properties commands.yml start.sh advertise.py stats.py /spigot/
COPY plugins plugins/
COPY --from=build /build/spigot-*.jar .

COPY --from=build /build/Dynmap-*.jar plugins/
COPY --from=build /build/jars/EssentialsX-*.jar plugins/
COPY --from=build /build/jars/EssentialsXAntiBuild*.jar plugins/
COPY --from=build /build/jars/EssentialsXChat*.jar plugins/
COPY --from=build /build/jars/EssentialsXProtect*.jar plugins/
COPY --from=build /build/jars/EssentialsXSpawn*.jar plugins/
COPY --from=build /build/Geyser-*.jar plugins/
COPY --from=build /build/archive/builder/build/libs/JoinCommands-*.jar plugins/
COPY --from=build /build/LuckPerms-Bukkit*.jar plugins/
COPY --from=build /build/Multiverse-Core*.jar plugins/
COPY --from=build /build/plotsquared-bukkit*.jar plugins/
COPY --from=build /build/Plot2Dynmap*.jar plugins/
COPY --from=build /build/ProtocolLib*.jar plugins/
COPY --from=build /build/Vault*.jar plugins/
COPY --from=build /build/WorldBorder*.jar plugins/
COPY --from=build /build/WorldEdit*.jar plugins/
RUN echo "eula=true" > eula.txt

RUN apt-get install nano
RUN chown spigot:spigot * -R
USER spigot

# This fails,
# RUN java -Xms1G -Xmx1G -jar minecraft_server.1.10.2.jar nogui
# TODO: create server.properties, and an eula.txt
CMD ["./start.sh"]
