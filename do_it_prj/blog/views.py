from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

#FBV로 페이지 만들기
def index(request):
    posts = Post.objects.all().order_by('-pk') #모든 Post 레코드를 가져와 posts에 저장
    #ㄴ 이런 방식으로 views.py에서 데이터베이스에 쿼리를 날려 원하는 레코드를 가져올 수 있다.

    return render(
        request,
        'blog/landing.html',
        {
            'posts' : posts, #render()함수안에 posts를 딕셔너리 형태로 추가
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )

#CBV로 페이지 만들기
# class PostList(ListView):
#     model = Post #ListView를 사용할 것이고, model은 Post다.
#     template_name = 'blog/landing.html'
# Create your views here.
