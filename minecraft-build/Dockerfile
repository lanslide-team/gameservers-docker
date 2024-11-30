FROM base:latest AS jdk
ARG spigot_version=latest
ENV SPIGOT_VERSION=${spigot_version}
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

RUN wget -O ps.zip https://github.com/IntellectualSites/PlotSquared/archive/refs/tags/7.4.0.zip
RUN unzip ps.zip
RUN /build/PlotSquared-*/gradlew

#RUN wget -O plt2dyn.zip https://ci.athion.net/job/Plot2Dynmap/lastSuccessfulBuild/artifact/build/libs/*zip*/libs.zip
#RUN unzip plt2dyn.zip
RUN wget https://github.com/IntellectualSites/Plot2Dynmap/releases/download/7.0.0/Plot2Dynmap-7.0.0.jar
#RUN rm ./libs/*-javadoc.jar
#RUN rm ./libs/*-sources.jar
RUN wget -O ess.zip https://ci.ender.zone/job/EssentialsX/lastSuccessfulBuild/artifact/jars/*zip*/jars.zip
RUN unzip ess.zip
RUN wget -O join.zip https://jenkins.sirblobman.xyz/job/SirBlobman/job/JoinCommands/job/main/lastSuccessfulBuild/artifact/*zip*/target.zip
RUN unzip join.zip
#RUN wget -O mv.zip http://ci.onarandombox.com/job/Multiverse-Core/lastSuccessfulBuild/artifact/target/*zip*/target.zip
#RUN unzip mv.zip
RUN wget "https://github.com/Multiverse/Multiverse-Core/releases/download/4.3.14/multiverse-core-4.3.14.jar"

RUN wget https://ci.dmulloy2.net/job/ProtocolLib/lastStableBuild/artifact/build/libs/ProtocolLib.jar
#RUN wget -O luckPerm.zip https://ci.lucko.me/view/LuckPerms/job/LuckPerms/lastSuccessfulBuild/artifact/bukkit/loader/build/libs/*zip*/libs.zip
#RUN unzip luckPerm.zip
RUN wget https://download.luckperms.net/1561/bukkit/loader/LuckPerms-Bukkit-5.4.146.jar

#https://dynmap.us/releases/Dynmap-3.6-spigot.jar
RUN wget https://github.com/user-attachments/files/17738419/Dynmap-3.7-beta-7_1.21.3_spigot.jar.zip && \
    unzip Dynmap-3.7-beta-7_1.21.3_spigot.jar.zip && \
    rm Dynmap-3.7-beta-7_1.21.3_spigot.jar.zip -f

RUN wget https://github.com/MilkBowl/Vault/releases/download/1.7.3/Vault.jar
RUN wget https://github.com/PryPurity/WorldBorder/releases/download/v2.1.5/WorldBorder.jar
RUN wget -O worldedit.jar https://dev.bukkit.org/projects/worldedit/files/latest
#RUN wget https://github.com/kangarko/ChatControl-Pro/releases/download/8.10.5/ChatControl-8.10.5.jar
## Moved to Premium version see README for more details

# server.properties

FROM jdk as final
ADD server.properties commands.yml start.sh advertise.py stats.py /spigot/
COPY plugins plugins/
#COPY --from=build /build/ChatControl-*.jar plugins/
COPY --from=build /build/spigot-*.jar .
COPY --from=build /build/Dynmap*.jar plugins/
COPY --from=build /build/Vault.jar plugins/
COPY --from=build /build/WorldBorder.jar plugins/
COPY --from=build /build/Plot2Dynmap-*.jar plugins/
#COPY --from=build /build/target/ProtocolLib*.jar plugins/
COPY --from=build /build/multiverse-Core-*.jar plugins/
COPY --from=build /build/archive/builder/build/libs/JoinCommands-*.jar plugins/
COPY --from=build /build/jars/EssentialsX-*.jar plugins/
COPY --from=build /build/jars/EssentialsXAntiBuild*.jar plugins/
COPY --from=build /build/jars/EssentialsXChat*.jar plugins/
COPY --from=build /build/jars/EssentialsXProtect*.jar plugins/
COPY --from=build /build/jars/EssentialsXSpawn*.jar plugins/
COPY --from=build /build/LuckPerms-Bukkit*.jar plugins/
Copy --from=build /build/worldedit.jar plugins/
RUN echo "eula=true" > eula.txt

RUN apt-get install nano
RUN chown spigot:spigot * -R
USER spigot

# This fails,
# RUN java -Xms1G -Xmx1G -jar minecraft_server.1.10.2.jar nogui
# TODO: create server.properties, and an eula.txt
CMD ["./start.sh"]
