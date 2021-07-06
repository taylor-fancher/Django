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
        'this_book': Book.objects.get(id=number),
    
    }
    return render(request, 'this_book.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all
    }
    return render(request, 'authors.html', context)

def create_author(request):
    author = Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST["last_name"],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def this_author(request, number):
    context = {
        'this_author': Author.objects.get(id=number)
    }
    return render(request, 'this_author.html', context)
# Create your views here.
