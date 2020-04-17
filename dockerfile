FROM jenkins/jenkins:lts

USER root

RUN pwd

RUN ls -la

RUN apt-get update

RUN apt-get install -y python3-pip

RUN pip3 install selenium

RUN pip3 install Html-TestRunner

RUN pip3 install chromedriver