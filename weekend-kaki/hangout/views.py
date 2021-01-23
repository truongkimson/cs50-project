from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, 'hangout/home.html', context)

@login_required
def profile(request):
    context = {}
    return render(request, 'hangout/profile.html', context)

@login_required
def create(request):
    context = {}
    return render(request, 'hangout/create.html', context)

@login_required
def list(request):
    active_hangouts = request.user.owned_hangouts.all()
    context = {'active_hangouts': active_hangouts,}
    return render(request, 'hangout/list.html', context)

@login_required
def discover(request):
    context = {}
    return render(request, 'hangout/discover.html', context)

@login_required
def detail(request, hangout_id):
    context = {'hangout_id': hangout_id}
    return render(request, 'hangout/detail.html', context)
