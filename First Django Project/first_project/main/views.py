from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def number(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder to edit blog number {number}')

def destroy(request, number):
    return redirect('/')
# Create your views here.
