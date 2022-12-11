# from django.contrib.gis.db.backends.postgis import models
from django.shortcuts import render, redirect

def landing(request):
    return render(
        request,
        'homepage/landing.html'
    )

# def landing(request):
#     return render(
#         request,
#         'homepage/landing.html'
#     )
# Create your views here.
