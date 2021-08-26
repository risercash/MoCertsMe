FROM python:3
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /site
COPY . /site
WORKDIR /site/
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt