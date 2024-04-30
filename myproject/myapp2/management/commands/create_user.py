from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **kwargs):
        user = User(name='Thor', email='thunder@god.com', password='secret', age=2500)
        user.save()
        self.stdout.write(f'{user}')
