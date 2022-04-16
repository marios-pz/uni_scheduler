# Dont try to build image, mongodb does not wish to connect 

FROM python:latest

RUN apt-get update && apt-get upgrade --yes

RUN apt-get install python3 --yes && apt-get install python3-pip --yes

RUN mkdir -p /app

COPY main.py .

COPY requirements.txt .

COPY app /app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py"]