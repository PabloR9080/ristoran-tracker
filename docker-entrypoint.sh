#!/bin/bash -x
python manage.py makemigrations || exit 1
python manage.py makemigrations ristoranApi || exit 1
python manage.py migrate --noinput || exit 1
python manage.py load_data restaurantes.csv || exit 0

exec "$@"
