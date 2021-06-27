from django.shortcuts import render, get_random_string

def index(request):
    return render(response, 'index.html')

def random(request):
    request.session
# Create your views here.
