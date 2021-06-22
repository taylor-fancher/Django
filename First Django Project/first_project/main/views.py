from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponse

def index(response):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(response):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(response):
    return redirect('/')

# Create your views here.
