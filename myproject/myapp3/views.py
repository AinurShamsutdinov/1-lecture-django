import slug
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Author, Post


# Create your views here.


def hello(request):
    return HttpResponse('Hello World from function!')


class HelloView(View):

    def get(self, request):
        return HttpResponse('Hello World from class!')


def year_post(request, year):
    text = 'some text for test from method year_post'
    # postst
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):

    def get(self, request, year, month):
        text = 'some text for test from class MonthPost'
        # posts for year and month
        return HttpResponse(f'Posts from{month}/{year}<br>{text}')


def post_detail(request, year, month, slug:slug):
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'What creates list faster list() or []',
        'content': 'Тестирование передачи кириллицы'
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {
        'name': 'John Connor',
        'text': 'Come with me if you want to live',
        'number': 56,
        'tag': '<h2>H2 tag just for test</h2>'
               }
    return render(request, 'myapp3/my_template.html', context)


class TemplIf(TemplateView):
    template_name = 'myapp3/templ_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello world!'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'red': 'October',
        'blue': 'Sky',
        'yellow': 'Sun',
        'white': 'Snow',
        'poor': 'hobo',
    }
    context = {
        'my_list': my_list,
        'my_dict': my_dict
    }
    return render(request, 'myapp3/templ_for.html', context)


def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
