from django.urls import path, include
from django import urls
from . import views

urlpatterns = [
    path('',views.landing,name='home'),
    path('notice/',views.notice,name='notice'),
    path('notice/<int:pk>', views.single_page, name='single_page'),
    path('notice_create/',views.notice_create,name='notice_create'),
    path('introduce/',views.introduce,name='introduce'),
    path('history/',views.history,name='history'),
    path('map/',views.map,name='map'),
    path('business/',views.business,name='business'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('recruit/',views.recruit),
    path('contact/',views.contact, name='contact'),
    path('contact_list/',views.account, name='account'),
    path('contact_list/<int:pk>/delete',views.account_delete, name='account_delete'),


    # path('single_pages/',include('single_pages.urls')),

]