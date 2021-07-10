from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def shows(request):
    context = {
        'shows': Show.objects.all
    }
    return render(request, 'shows.html', context)

def one_show(request):
    pass

def edit_show(request):
    pass

def delete_show(request):
    pass

def add_show(request):
    pass


# Create your views here.
