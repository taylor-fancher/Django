from django.shortcuts import render, redirect
from .models import Show

def index(request):
    return render(request, 'index.html')

def shows(request):
    context = {
        'shows': Show.objects.all
    }
    return render(request, 'shows.html', context)

def one_show(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }
    return render(request,'one_show.html', context)

def edit_show(request):
    pass

def delete_show(request):
    pass

def add_show(request):
    return render(request, 'new_show.html')

def create(request):
    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc =  request.POST['desc']
    )
    return redirect('/shows')


# Create your views here.
