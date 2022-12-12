from django.urls import path, include
from django import urls
from . import views

urlpatterns = [
    path('',views.landing),
    path('about/',views.about),
    path('recruit/',views.recruit),
    path('contact/',views.contact),
    # path('single_pages/',include('single_pages.urls')),


]