FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /tech_task
WORKDIR /tech_task

COPY requirements.txt /tech_task/
COPY . /tech_task/

RUN pip install -r requirements.txt

RUN mkdir -p /back_media
RUN mkdir -p /back_static
