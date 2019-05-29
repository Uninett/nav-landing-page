FROM debian:stretch

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN sed 's/^deb /deb-src /' /etc/apt/sources.list >> /etc/apt/sources.list.d/debsrc.list

RUN apt-get -y update && apt-get install -y locales \
    && echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && locale-gen \
    && echo 'Europe/Oslo' > /etc/timezone && cp /usr/share/zoneinfo/Europe/Oslo /etc/localtime

RUN apt-get update && apt-get -y install python-pip gunicorn
RUN apt-get -y --no-install-recommends build-dep python-imaging python-psycopg2

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
RUN cd /app; /app/set-production-settings.sh


EXPOSE 8000
VOLUME ["/app"]
ENV DJANGO_SETTINGS_MODULE nav_landing_page.settings
ENV PYTHONPATH /app
CMD ["/app/docker-entrypoint.sh"]
