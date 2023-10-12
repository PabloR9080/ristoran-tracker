#!/bin/bash -x

python manage.py migrate --noinput || exit 1
python manage.py load_data restaurantes.csv

exec "$@"
