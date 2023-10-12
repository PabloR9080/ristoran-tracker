from django.core.management.base import BaseCommand
from ristoranApi.models import UserAPI

class Command(BaseCommand):
    help = 'Create admin account if it does not exist'

    def handle(self, *args, **options):
        if UserAPI.objects.count() == 0:
            UserAPI.objects.create_superuser('root@localhost','admin')
        else:
            print('Admin accounts can only be initialized if no Accounts exist')