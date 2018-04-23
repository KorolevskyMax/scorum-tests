FROM python:3.5-alpine

ADD . /tests
WORKDIR /tests
RUN pip install -r requirements.txt
WORKDIR features