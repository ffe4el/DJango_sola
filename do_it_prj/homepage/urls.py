from django.urls import path, include
from django import urls
from . import views

urlpatterns = [
    path('',views.landing),
    # path('single_pages/',include('single_pages.urls')),
    # path('',views.landing),

]