from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

#FBV로 페이지 만들기
# def index(request):
#     posts = Post.objects.all().order_by('-pk') #모든 Post 레코드를 가져와 posts에 저장
#     #ㄴ 이런 방식으로 views.py에서 데이터베이스에 쿼리를 날려 원하는 레코드를 가져올 수 있다.
#
#     return render(
#         request,
#         'blog/landing.html',
#         {
#             'posts' : posts, #render()함수안에 posts를 딕셔너리 형태로 추가
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )

#CBV로 페이지 만들기
class PostList(ListView):
    model = Post #ListView를 사용할 것이고, model은 Post다.
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

#FBV로 category_page() 함수 만들기
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )
# Create your views here.
