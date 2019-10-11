from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def gallery(request):
    return render(request, 'gallery.html')


