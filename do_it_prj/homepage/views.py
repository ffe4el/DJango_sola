# from django.contrib.gis.db.backends.postgis import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Topic, Reply
from django.http import HttpResponse

def landing(request):
    return render(
        request,
        'homepage/landing.html'
    )
def about(request):
    return render(
        request,
        'homepage/services.html'
    )
def notice(request):
    topics = Topic.objects.all().order_by('-pk')
    return render(
        request,
        'homepage/notice.html',
        {
            'topics': topics,
        }
    )

def single_page(request, pk):
    topic = Topic.objects.get(pk=pk)
    return render(
        request,
        'homepage/notice_detail.html',
        {
            'topic': topic,
        }
    )

def notice_create(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            message=message,
            writter=user
        )

        post = Reply.objects.create(
            message=message,
            created_by=user

        )

        return redirect('notice')

    return render(request, 'homepage/notice_create.html', {'topics': topics})

def introduce(request):
    return render(
        request,
        'homepage/introduce.html'
    )

def history(request):
    return render(
        request,
        'homepage/history.html'
    )

def business(request):
    return render(
        request,
        'homepage/business.html'
    )

def map(request):
    return render(
        request,
        'homepage/map.html'
    )

def recruit(request):
    return render(
        request,
        'homepage/recruit.html'
    )
def contact(request):
    return render(
        request,
        'homepage/contact.html'
    )

# Create your views here.
