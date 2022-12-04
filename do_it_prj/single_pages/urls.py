from django.urls import path
from django import urls
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    # path('', views.landing),
    # path('create_port/', views.PostCreate.as_view()),
    # path('new_port/', views.PostCreate.as_view())
    path('', views.index),
    path('detail/<int:pk>', views.single_post_page, name='single_post_page'),
    # path('detail/<int:pk>', views.PostDetail.as_view(), name='detail'),
    path('create/', views.PostCreate.as_view(), name='create'),
    # path('create/', views.fbv_create, name='fbv_create'),
    path('delete/<int:pk>',views.PostDelete.as_view(), name='delete'),
    path('update/<int:pk>',views.PostUpdate.as_view(), name='update'),
]