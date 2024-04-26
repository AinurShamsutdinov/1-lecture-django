import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, world!')


def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops, something went wrong.')
    else:
        logger.debug('About page accessed')
        return HttpResponse('This is about page.')

