FROM python:3.5-alpine

ADD requirements.txt /tests/
WORKDIR /tests
RUN pip install -r requirements.txt
ADD . /tests
WORKDIR features