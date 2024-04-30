from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Get users with name start with <Letter>.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name stars with')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        # istartswith operator to get values where name starts with letters
        user = User.objects.filter(name__istartswith=name)
        self.stdout.write(f'{user}')
