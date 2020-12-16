from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow World! This is the index page.")
# Create your views here.
