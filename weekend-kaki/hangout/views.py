from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'hangout/index.html', context)

def profile(request):
    request.session['random_para'] = 1
    context = {'session': request.session}
    return render(request, 'hangout/profile.html', context)
