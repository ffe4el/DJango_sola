from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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

class PostCreate(CreateView):
    model= Post
    fields=['name', 'head_image', 'hook_text', 'port1', 'port2', 'about_me', "profile_image"]

def new_port(request):

    name = request.GET.get('name')
    head_image = request.GET.get('head_image')
    hook_text = request.GET.get('head_image')
    port1 = request.GET.get('port1')
    port2 = request.GET.get('port2')
    about_me = request.GET.get('about_me')
    profile_image = request.GET.get('profile_image')


    context = {

        'name': name,

        'head_image': head_image,

        'hook_text': hook_text,

        'port1': port1,

        'port2': port2,

        'about_me': about_me,

        'profile_image': profile_image

    }

    return render(request, 'single_pages/new_port.html', context)
# Create your views here.
