# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /cinema
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /cinema/
