from random import choices

from django.core.management import BaseCommand

from myapp3.models import Author, Post

LOREM = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore '
         'magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea '
         'commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat '
         'nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit '
         'anim id est laborum.')


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    author=author,
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64))
                )
                post.save()
