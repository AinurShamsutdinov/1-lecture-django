from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Get user by id'

    # add_arguments позволяет парсить командную строку
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User Id')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.get(id=id)
        self.stdout.write(f'{user}')
