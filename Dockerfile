FROM python:3.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY ./ ./