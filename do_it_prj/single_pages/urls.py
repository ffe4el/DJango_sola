from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
    path('create_port/', views.PostCreate.as_view()),
    path('new_port/', views.PostCreate.as_view())
]