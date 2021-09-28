FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt install -y python3-pip

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]