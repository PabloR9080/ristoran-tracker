import csv
from django.core.management.base import BaseCommand
from ristoranApi.models import Restaurant
from django.db import transaction
class Command(BaseCommand):
    help = 'Load data from a CSV file into the database.'
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        #with transaction.atomic():
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                restaurant_data = {
                    '_id': row['id'],
                    'rating': row['rating'],
                    'name': row['name'],
                    'site': row['site'],
                    'email': row['email'],
                    'phone': row['phone'],
                    'street': row['street'],
                    'city': row['city'],
                    'state': row['state'],
                    'lat': row['lat'],
                    'lng': row['lng'],
                }
                Restaurant.objects.create(**restaurant_data)
