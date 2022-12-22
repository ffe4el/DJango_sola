# from django.contrib.gis.db.backends.postgis import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Topic, Reply, Account
from django.http import HttpResponse
from team_post.models import room, talk

def landing(request):
    rooms = room.objects.all()
    topics = Topic.objects.all().order_by('-pk')
    return render(
        request,
        'homepage/landing.html',
        {
            'topics': topics,
            'rooms': rooms,
        }
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


def portfolio(request):
    return render(
        request,
        'homepage/portfolio.html'
    )


def recruit(request):
    return render(
        request,
        'homepage/recruit.html'
    )


def account(request):
    accounts = Account.objects.all().order_by('-pk')
    return render(
        request,
        'homepage/contact_list.html',
        {
            'accounts': accounts,
        }
    )

def account_delete(request,pk):
    accounts = Account.objects.get(pk=pk)
    accounts.delete()
    return redirect('account')

def contact(request):
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

        return redirect('/contact')

    return render(request, 'homepage/contact.html', {'accounts': accounts})

# Create your views here.
