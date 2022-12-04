# from django.contrib.gis.db.backends.postgis import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from . import models
from .models import Post
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

# class PostCreate(CreateView):
#     model= Post
#     fields=['name', 'head_image', 'hook_text', 'port1', 'port2', 'about_me', "profile_image"]
#     template_name = 'blog/post_detail.html'

# def new_port(request):
    #
    # name = request.GET.get('name')
    # head_image = request.GET.get('head_image')
    # hook_text = request.GET.get('head_image')
    # port1 = request.GET.get('port1')
    # port2 = request.GET.get('port2')
    # about_me = request.GET.get('about_me')
    # profile_image = request.GET.get('profile_image')
    #
    #
    # context = {
    #
    #     'name': name,
    #
    #     'head_image': head_image,
    #
    #     'hook_text': hook_text,
    #
    #     'port1': port1,
    #
    #     'port2': port2,
    #
    #     'about_me': about_me,
    #
    #     'profile_image': profile_image
    #
    # }
    # return render(request, 'single_pages/post_detail.html')
    # return render(request, 'single_pages/post_detail.html', context)
class PostList(ListView):
    model= models.Post
    context_object_name = 'post'
    template_name = 'single_pages/post_list.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = models.Post
    template_name = 'single_pages/post_detail.html'

class PostCreate(CreateView):
    model=Post
    fields =['name', 'head_image', 'hook_text', 'port1', 'port2',]
    success_url = '/'
    template_name = 'single_pages/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.address = form.cleaned_data['head_image']

        post.save()
        return super().form_valid(form)
        # return HttpResponseRedirect(self.get_success_url())

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
