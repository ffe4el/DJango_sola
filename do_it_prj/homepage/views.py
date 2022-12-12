# from django.contrib.gis.db.backends.postgis import models
from django.shortcuts import render, redirect

def landing(request):
    return render(
        request,
        'homepage/landing.html'
    )
def about(request):
    return render(
        request,
        'homepage/services.html'
    )
def recruit(request):
    return render(
        request,
        'homepage/articles.html'
    )
def contact(request):
    return render(
        request,
        'homepage/contact.html'
    )
# Create your views here.
