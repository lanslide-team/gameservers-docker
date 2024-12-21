FROM base:latest AS jdk
ARG spigot_version=1.21.4
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


#RUN git clone https://github.com/webbukkit/dynmap
#RUN /build/PlotSquared-*/gradlew init --overwrite
#RUN cd dynmap && ./gradlew build

#RUN wget https://github.com/user-attachments/files/17738419/Dynmap-3.7-beta-7_1.21.3_spigot.jar.zip && \
#    unzip Dynmap-3.7-beta-7_1.21.3_spigot.jar.zip && \
#    rm Dynmap-3.7-beta-7_1.21.3_spigot.jar.zip -f

RUN wget https://starcatcher.us/Jacob/Dynmap-3.7-beta-7-spigot.zip && \
    unzip Dynmap-3.7-beta-7-spigot.zip && \
    rm Dynmap-3.7-beta-7-spigot.zip -f
#RUN wget https://cdn.modrinth.com/data/fRQREgAc/versions/AdtrWcU2/Dynmap-3.7-beta-7-spigot.jar
#https://cdn.modrinth.com/data/fRQREgAc/versions/QtTWJjW6/Dynmap-3.7-beta-6-spigot.jar
#https://cdn.modrinth.com/data/fRQREgAc/versions/5F9fwzR1/Dynmap-3.7-beta-6-spigot.jar
#https://dynmap.us/releases/Dynmap-3.6-spigot.jar

RUN wget -O Geyser-Spigot.jar https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot

FROM jdk as final
ADD server.properties advertise.py stats.py /spigot/
COPY plugins plugins

#COPY --from=build /build/ChatControl-*.jar plugins/
COPY --from=build /build/Geyser-*.jar plugins/
COPY --from=build /build/spigot-*.jar .
COPY --from=build /build/Dynmap*.jar plugins/
#COPY --from=build /build/dynmap/ plugins/dynmap-build

RUN echo "eula=true" > eula.txt

RUN apt-get install nano
RUN chown spigot:spigot * -R
USER spigot

# This fails,
# RUN java -Xms1G -Xmx1G -jar minecraft_server.1.10.2.jar nogui
# TODO: create server.properties, and an eula.txt
CMD ["./start.sh"]
