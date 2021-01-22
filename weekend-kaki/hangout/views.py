from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'hangout/home.html', context)

def profile(request):
    request.session['random_para'] = 1
    context = {'session': request.session}
    return render(request, 'hangout/profile.html', context)

def create(request):
    request.session['random_para'] = 1
    context = {'session': request.session}
    return render(request, 'hangout/create.html', context)

def list(request):
    request.session['random_para'] = 1
    context = {'session': request.session}
    return render(request, 'hangout/list.html', context)

def discover(request):
    request.session['random_para'] = 1
    context = {'session': request.session}
    return render(request, 'hangout/discover.html', context)