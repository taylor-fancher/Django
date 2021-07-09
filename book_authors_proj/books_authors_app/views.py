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

def this_book(request, id):
    context = {
        'this_book': Book.objects.get(id=id),
        'authors': Author.objects.all
    }
    return render(request, 'this_book.html', context)

def add_author(request):
    this_book = Book.objects.get(id=request.POST['book'])
    this_author = Author.objects.get(id=request.POST['author'])
    this_book.authors.add(this_author)
    return redirect(f'/book/{this_book.id}')

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

def this_author(request, id):
    context = {
        'this_author': Author.objects.get(id=id)
    }
    return render(request, 'this_author.html', context)
# Create your views here.
