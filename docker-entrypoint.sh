#!/bin/sh -e
# Ensure db schema is up to date on app start
python /app/manage.py migrate --noinput
python /app/manage.py collectstatic --noinput
exec gunicorn -b 0.0.0.0:8000 wsgi
