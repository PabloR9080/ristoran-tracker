from django.core.management.base import BaseCommand
from ristoranApi.models import UserAPI

class Command(BaseCommand):
    help = 'Create admin account if it does not exist'

    def handle(self, *args, **options):
        if UserAPI.objects.filter(is_superuser=True).count() == 0:
            try:
                UserAPI.objects.create_superuser('root@localhost','admin')
            except Exception as e:
                print('Error creating admin account: {}'.format(e))
        else:
            print('Admin accounts can only be initialized if no Accounts exist')