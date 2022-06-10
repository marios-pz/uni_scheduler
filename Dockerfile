FROM alpine:latest

ENV TZ=Etc/UTC

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
echo $TZ > /etc/timezone

ADD . /uni_scheduler
WORKDIR /uni_scheduler

RUN apk update && \
apk upgrade && \
apk add python3 py3-pip && \
pip install -r requirements.txt && \
cp -r webapp/* .

CMD python3 server.py && \
sleep infinity

HEALTHCHECK CMD /DockerHealthcheck.sh
