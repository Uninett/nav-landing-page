FROM mbrekkevold/wheezy-no

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y --no-install-recommends install python-pip gunicorn

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
