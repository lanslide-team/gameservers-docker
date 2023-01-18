FROM ubuntu:22.04
ARG TZ="Etc/UTC"
RUN sed -i 's/archive.ubuntu.com/au.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt-get update  && apt-get dist-upgrade -y &&\
        apt-get install -y unzip p7zip-full curl wget iproute2 vim-tiny bzip2 jq software-properties-common apt-transport-https && \
        apt-get clean
RUN echo "$TZ" > /etc/timezone
RUN  ln -fs /usr/share/zoneinfo/$TZ /etc/localtime

