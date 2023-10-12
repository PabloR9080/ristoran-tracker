#!/bin/bash -x
python manage.py makemigrations --noinput || exit 1
python manage.py makemigrations ristoranApi --noinput || exit 1
python manage.py migrate --noinput || exit 1
python manage.py load_data restaurantes.csv || exit 1

exec "$@"
