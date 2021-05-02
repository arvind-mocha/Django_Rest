# python image
FROM python:3.7-alpine

# Maintainer name
LABEL maintainer='ARVIND'

# Just to make sure no partial outputs
ENV PYTHONUNBUFFERED 1

# Copying requirements.txt from local env to docker
COPY ./requirements.txt /requirements.txt  

# For Postgres sql Database, permanent dependecies
RUN apk add --update --no-cache postgresql-client jpeg-dev

# temporary dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

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

# creating two directories for our upload images and our static files
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# creating a user to run only this application instead of using root user, this is for security purpose
# if we don't do this our image will run using the root account
RUN adduser -D user

# giving permision to all folders inside vol to our user
RUN chown -R user:user /vol/

# user name is user
USER user


# docker build . is the command used to build our image after configuring the Dockerfile