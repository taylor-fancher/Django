from django.shortcuts import render
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'index.html')

def random(request):
    pass
# Create your views here.
