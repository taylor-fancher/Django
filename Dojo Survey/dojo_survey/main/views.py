from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    return redirect('/results')

def results(request):
    context = {
        'name': request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language']
    }
    return render(request, 'results.html', context)
# Create your views here.
