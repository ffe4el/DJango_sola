from django.urls import path
from django import urls
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
    # path('create_port/', views.PostCreate.as_view()),
    # path('new_port/', views.PostCreate.as_view())
    path('post/', views.PostList.as_view(), name='post'),
    path('new_post/', views.PostCreate.as_view(), name='create'),
    path('delete/<int:pk>',views.PostDelete.as_view(), name='delete'),
    path('update/<int:pk>',views.PostUpdate.as_view(), name='update'),
]