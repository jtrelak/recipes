FROM ubuntu:bionic

RUN apt-get update
RUN apt-get -y install wget
RUN apt-get update
RUN apt-get -y install  default-jdk
RUN apt-get update
RUN apt-get -y install libcurl3
RUN apt-get update
RUN apt-get -y install libcairo2
RUN apt-get update
RUN apt-get -y install libgdk-pixbuf2.0-0
RUN apt-get update
RUN apt-get -y install libgtk2.0-0
RUN apt-get update
RUN apt-get -y install libgtk-3-0
RUN apt-get update
RUN apt-get -y install libpango1.0-0
RUN apt-get update
RUN apt-get -y install libxcursor1
RUN apt-get update
RUN apt-get -y install libxss1
RUN apt-get update
RUN apt-get -y install xdg-utils
RUN wget https://launcher.mojang.com/download/Minecraft.deb
RUN dpkg -i Minecraft.deb
RUN groupadd -g 1000 jtrelak
RUN useradd -d /home/jtrelak -s /bin/bash -m jtrelak -u 1000 -g 1000
USER jtrelak
ENV HOME /home/jtrelak
CMD /usr/bin/minecraft-launcher
