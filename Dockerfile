FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install cron && apt-get -y install pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY .env.example /code/.env
RUN cat /code/.env
ADD . /code/