from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
        messages.error(request, 'Email does not exist.')
        return redirect('/')

def register(request):
    return render(request, 'register.html')

def new_user(request):
    errors = User.objects.user_validator(request.POST)

    user = User.objects.filter(email=request.POST['email'])
    if user:
        messages.error(request, 'Email already exists.')
        return redirect('/register')

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user1 = User.objects.create(
        name = request.POST['name'],
        alias = request.POST['alias'],
        email = request.POST['email'],
        password = hashed_pw,
    )
    request.session['log_user_id'] = user1.id
    return redirect('/dashboard')

def dashboard(request):
    context = {
        'user': User.objects.get(id=request.session['log_user_id']),
        'books': Book.objects.all(),
        'reviews': Review.objects.order_by('-created_at')[:3]
    }
    return render(request, 'dashboard.html', context)

def add_book_review(request):
    context = {
        'user': User.objects.get(id=request.session['log_user_id'])
    }
    return render(request, 'add_book_review.html', context)

def create_book_review(request):
    errors = Book.objects.book_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/add_book_review')
    
    book1 = Book.objects.create(
        title = request.POST['title'],
        author = request.POST['author'],
    )

    errors = Review.objects.review_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/add_book_review')
    
    review = Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        created_by = User.objects.get(id=request.session['log_user_id']),
        review_of = Book.objects.get(id=book1.id)
    )
    return redirect ('/dashboard')

def one_book(request, id):
    context = {
        'user': User.objects.get(id=request.session['log_user_id']),
        'book': Book.objects.get(id=id),
    }
    return render(request, 'one_book.html', context)

def add_review(request):
    book = Book.objects.get(id=request.POST['review_of'])

    errors = Review.objects.review_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/book/{book.id}')
    
    review = Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        created_by = User.objects.get(id=request.POST['created_by']),
        review_of = Book.objects.get(id=request.POST['review_of']),
    )
    return redirect(f'/book/{book.id}')
# Create your views here.
