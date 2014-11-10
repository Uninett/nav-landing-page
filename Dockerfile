FROM mbrekkevold/wheezy-no

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y --no-install-recommends install python-pip

RUN apt-get -y --no-install-recommends build-dep python-imaging python-psycopg2

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /web

EXPOSE 8000
VOLUME /web
CMD ["python", "/web/manage.py", "runserver", "0.0.0.0:8000"]
