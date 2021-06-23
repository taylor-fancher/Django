from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponse

def index(response):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(response):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(response):
    return redirect('/')

def number(response, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(response, number):
    return HttpResponse(f'placeholder to edit blog number {number}')

def destroy(response, number):
    return redirect('/')
# Create your views here.
