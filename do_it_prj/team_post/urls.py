from django.urls import path
from . import views


urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('<str:room_name>/', views.chat_room, name='chat_room')
]
