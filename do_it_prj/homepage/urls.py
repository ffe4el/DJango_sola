from django.urls import path, include
from django import urls
from . import views

urlpatterns = [
    path('',views.landing),
    path('about/',views.about),
    path('notice/',views.notice,name='notice'),
    path('notice_create/',views.notice_create,name='notice_create'),
    path('introduce/',views.introduce,name='introduce'),
    path('history/',views.history,name='history'),
    path('map/',views.map,name='map'),
    path('business/',views.business,name='business'),
    path('recruit/',views.recruit),
    path('contact/',views.contact),

    # path('single_pages/',include('single_pages.urls')),


]