FROM python:latest

RUN mkdir /src
WORKDIR /src
COPY . /src
RUN pip3 install -r requirements.txt