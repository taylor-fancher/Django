from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def shows(request):
    pass


# Create your views here.
