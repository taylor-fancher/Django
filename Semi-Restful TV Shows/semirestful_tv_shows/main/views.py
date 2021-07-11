from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show

def index(request):
    return redirect('/shows')

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

def update(request, id):
    this_show = Show.objects.get(id=id)
    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.release_date = request.POST['release_date']
    this_show.desc = request.POST['desc']
    this_show.save()
    return redirect(f'/shows/{this_show.id}')

def edit_show(request, id):
    context = {
        'this_show': Show.objects.get(id=id),
    }
    return render(request, 'edit_show.html', context)

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

def add_show(request):
    return render(request, 'new_show.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/new')

    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    desc = request.POST['desc']

    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc =  request.POST['desc']
    )
    return redirect('/shows')


# Create your views here.
