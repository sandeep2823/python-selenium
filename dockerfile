FROM selenium/standalone-chrome as ssc
FROM debian:jessie
FROM jenkins/jenkins:lts

USER seluser

# Install dependencies from selenium standalone chrome image
COPY --from=ssc /opt/bin/entry_point.sh /opt/bin/entry_point.sh
EXPOSE 4444

USER root

# Install base dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y -q --no-install-recommends \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        libssl-dev \
        python3-pip \
        rsync \
        software-properties-common \
        devscripts \
        autoconf \
        ssl-cert \
    && apt-get clean

RUN python3 --version

# Install Chrome & Chrome Driver for Chrome Browser
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

RUN apt-get install unzip

RUN wget https://chromedriver.storage.googleapis.com/2.39/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && mv chromedriver /usr/bin/ \
    && rm chromedriver_linux64.zip

RUN pip3 install Html-TestRunner

RUN pip3 install chromedriver

COPY . /var/jenkins_home/workspace/sel
