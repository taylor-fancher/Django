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

    user = User.objects.filer(email=request.POST['email'])
    if user:
        messages.error(request, 'Email already exists.')
        return redirect('/register')

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrpyt.gensalt()).decode()

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
        'reviews': Review.objects.latest('created_at')[:3]
    }
    return render(request, 'dashboard.html', context)
# Create your views here.
