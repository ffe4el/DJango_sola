from django.urls import path
from . import views

urlpatterns = [
    # 이부분을 채워서 urls 주소를 불러 줄것이다~!

    #FBV로 페이지 만들기
    path('<int:pk>/', views.single_post_page),
    path('', views.index),

    #CBV로 페이지 만들기
    # path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_pages),
]