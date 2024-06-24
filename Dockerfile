FROM python:3.10.1-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y nano less htop supervisor \
    curl postgresql-client libssl-dev openssl binutils libproj-dev gdal-bin libgdal-dev \
    apt-transport-https ca-certificates gnupg tree rsync time screen --no-install-recommends
RUN apt update && apt install x11vnc xvfb fluxbox dumb-init rsync -y

RUN mkdir /code
WORKDIR /code

RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

COPY pip-cached-install.sh pyproject.toml poetry.lock ./
RUN bash ./pip-cached-install.sh

ADD . /code/

ENV DUMB_INIT_SETSID 0
EXPOSE 8080 1717
ENTRYPOINT ["dumb-init", "--"]
