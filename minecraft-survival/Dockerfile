FROM base:latest AS jdk
ARG spigot_version=latest
ENV SPIGOT_VERSION=${spigot_version}
ARG java_version=17
ENV JAVA_VERSION=${java_version}
# todo: collapse these to single command
RUN sed --in-place --regexp-extended "s/(\/\/)(archive\.ubuntu)/\1au.\2/" /etc/apt/sources.list \
    && apt-get install -y software-properties-common \ 
    && apt-add-repository ppa:openjdk-r/ppa && \
       apt-get update
RUN apt-get install -y ca-certificates-java zip
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

# Download Deathrun
RUN wget -O Deathrun.zip \ 
    "https://pcminecraft-mods.com/wp-content/uploads/2023/06/Deathrun_Ultimate_II.zip" && \ 
    unzip Deathrun.zip "Deathrun Ultimate II/*" -d "deathrun" && \
    rm Deathrun.zip
   #  unzip Deathrun2.zip -d /spitgot && rm Deathrun*.zip -f

FROM jdk as final
ADD server.properties commands.yml start.sh stats.py advertise.py /spigot/
#COPY plugins plugins/
COPY --from=build /build/spigot-*.jar .
COPY --from=build /build/deathrun . 

RUN mv "/spigot/Deathrun Ultimate II/" /spigot/deathrun

RUN echo "eula=true" > eula.txt

RUN apt-get install nano
RUN chown spigot:spigot * -R
USER spigot

CMD ["./start.sh"]
