from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    return render(request, 'index.html')

def books(request):
    context = {
        'books': Book.objects.all
    }
    return render(request, 'books.html', context)

def create_book(request):
    book = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect ('/books')

def this_book(request, number):
    context = {
        'books': Book.objects.all
    }
    return render(request, 'this_book.html', context)

def authors(request):
    return render(request, 'authors.html')

# Create your views here.
