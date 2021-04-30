# python image
FROM python:3.7-alpine

# Maintainer name
LABEL maintainer='ARVIND'

# Just to make sure no partial outputs
ENV PYTHONUNBUFFERED 1

# Copying requirements.txt from local env to docker
COPY ./requirements.txt /requirements.txt  

# For Postgres sql Database
RUN apk add --update --no-cache postgresql-client

# temporary dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev

# installs the requirements.txt which is copied from the local env into docker
RUN pip install install -r /requirements.txt

# deleting temporary dependencies for postgres
RUN apk del .tmp-build-deps

# creating a directory inside docker
RUN mkdir /app

# making that directory as the working directory
WORKDIR /app

# Copying the app directory from local machine to docker
COPY ./app /app

# creating a user to run only this application instead of using root user, this is for security purpose
# if we don't do this our image will run using the root account
RUN adduser -D user

# user name is user
USER user


# docker build . is the command used to build our image after configuring the Dockerfile