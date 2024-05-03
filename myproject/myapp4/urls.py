from django.urls import path
from .views import user_form, many_fields_form, add_user, image_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('user/', add_user, name='add_user'),
    path('image/', image_form, name='image_form')
]
