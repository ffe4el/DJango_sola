# from django.contrib.gis.db.backends.postgis import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from . import models
from .models import Post
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )


def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'single_pages/post_list.html',
        {
            'posts': posts,
        }
    )

# class PostList(ListView):
#     model= models.Post
#     context_object_name = 'post'
#     template_name = 'single_pages/post_list.html'
#     ordering = '-pk'


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'single_pages/post_detail.html',
        {
            'post': post
        }
    )

# class PostDetail(DetailView):
#     model = models.Post
#     template_name = 'single_pages/post_detail.html'

# def fbv_create(request):
#     model = Post
#     if request.method == 'POST':
#         print("포트폴리오 생성")
#         model.name = request.POST['name']
#         model.head_image = request.FILES['head_image']
#         model.hook_text = request.POST['hook_text']
#         model.port1 = request.POST['port1']
#         model.port2 = request.POST['port2']
#         model.save()
#         return redirect(reverse(''))  # reverse는 url의 name으로 연결시켜준다.
#
#     return render(request, 'single_pages/post_form.html')


class PostCreate(CreateView):
    model = Post
    fields =['name', 'head_image', 'hook_text', 'port1', 'port2',]
    success_url = '/'
    # template_name = 'single_pages/post_form.html'

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.address = form.cleaned_data['head_image']
    #
    #     post.save()
    #     return super().form_valid(form)
    #     return HttpResponseRedirect(self.get_success_url())

#Delete(게시물 삭제)
class PostDelete(DeleteView) :
    model = Post
    template_name ='single_pages/delete.html'
    success_url='/' # or reverse_lazy('designer') url 이름


# Update(게시물 수정)
class PostUpdate(UpdateView):
    model = Post
    fields = ['name', 'head_image', 'hook_text', 'port1', 'port2', ]
    template_name = 'single_pages/update.html'
    success_url = '/'  # or reverse_lazy('designer') url 이름

    # def form_valid(self, form):
    #     designer = form.save(commit=False)
    #     designer.adress =form.cleaned_data['image']

    #     designer.save()
    #     return super().form_valid(form)



def port(request):
    return render(request, 'single_pages/post_detail.html')
# Create your views here.
