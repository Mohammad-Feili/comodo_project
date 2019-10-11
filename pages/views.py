from django.shortcuts import render


def price(request):
    return render(request, 'price.html')


def games(request):
    return render(request, 'games.html')


def elements(request):
    return render(request, 'elements.html')
