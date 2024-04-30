from django.urls import path, include
from . import views

urlpatterns = [
    path('prefix/', views.index, name='index'),
    path('about/', views.about, name='about'),
]
