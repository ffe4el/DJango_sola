# from django.contrib.gis.db.backends.postgis import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from . import models
from .models import Post
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from homepage.models import Account

# def landing(request):
#     return render(
#         request,
#         'single_pages/landing.html'
#     )

# def about_me(request):
#     return render(
#         request,
#         'single_pages/about_me.html'
#     )



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
    accounts = Account.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        account = Account.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return redirect('single_post_page', pk)
    return render(
        request,
        'single_pages/post_detail.html',
        {
            'post': post,
            'accounts': accounts,
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
    fields = ['type', 'name', 'head_image', 'hook_text', 'port1_title', 'port1', 'port1_img', 'port2_title', 'port2',
              'port2_img', 'port3_title', 'port3', 'port3_img','port4_title', 'port4',
              'port4_img', 'port5_title', 'port5', 'port5_img', 'port6_title', 'port6',
              'port6_img', 'profile_image', 'about_me', ]
    success_url = '/single_pages'


# def create(request):
#     posts=Post.objects.all()
#     redirect('/single_pages')
#     return render(request,'homepage/post_form.html', {'posts': posts})



#Delete(게시물 삭제)
class PostDelete(DeleteView):
    model = Post
    template_name ='single_pages/delete.html'
    success_url='/single_pages' # or reverse_lazy('designer') url 이름

# def delete(request,pk):
#     posts = Post.objects.get(pk=pk)
#     posts.delete()
#     return redirect('index')



# Update(게시물 수정)
class PostUpdate(UpdateView):
    model = Post
    # fields = ['type', 'name', 'head_image', 'hook_text', 'profile_image', 'about_me',]
    fields = ['type','name', 'head_image', 'hook_text', 'port1_title','port1','port1_img', 'port2_title','port2', 'port2_img','port3_title','port3','port3_img',
              'port4_title','port4','port4_img','port5_title','port5','port5_img', 'port6_title', 'port6','port6_img','profile_image', 'about_me',]
    template_name = 'single_pages/update.html'
    success_url = '/single_pages'  # or reverse_lazy('designer') url 이름
    # def form_valid(self, form):
    #     designer = form.save(commit=False)
    #     designer.adress =form.cleaned_data['image']
    #
    #     designer.save()
    #     return super().form_valid(form)

# def update(request,pk):
#     posts = Post.objects.get(pk=pk)
#     if request.method == 'POST':
#         name = request.POST['name']
#         hook_text = request.POST['hook_text']
#
#         post = Post.objects.create(
#             name=name,
#             hook_text=hook_text,
#
#         )
#         return redirect('index')
#     return render(request, 'homepage/update.html', {'posts': posts})



# def port(request):
#     return render(request, 'single_pages/post_detail.html')
# Create your views here.
