import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User

logger = logging.getLogger(__name__)


# Create your views here.
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            #doing something with data
            logger.info(f'Recieved {name=}, {email=}, {age=}.')
            print(f'Recieved {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST)
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # doing something with data
            logger.info(f'Recieved {form.cleaned_data}')
            print(f'Recieved {form.cleaned_data}')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})


def add_user(request):
    message: str = 'Placeholder'
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Data Error'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            #doing something with data
            logger.info(f'Recieved {name=}, {email=}, {age=}.')
            print(f'Recieved {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'User added'
    else:
        form = UserForm()
        message = 'Fill the form'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def image_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})
