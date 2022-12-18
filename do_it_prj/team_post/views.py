from django.shortcuts import render, redirect, reverse

from .models import talk, room
from datetime import datetime


# Create your views here.
def chat_room(request, room_name):
    talks = talk.objects.all()
    if request.method == "POST":
        massage = request.POST.get('massage')
        writter = request.user
        time_stamp = datetime.now()
        files = request.FILES.get("files")

        talks = talk.objects.create(
            massage=massage,
            writter=writter,
            time_stamp=time_stamp,
            files=files,

        )


        return redirect('chat_room',room_name)

    return render(request, 'team_post/chat_room.html', context={
        "talks": talks,
        "room_name": room_name,
    })


def lobby(request):
    if request.method == "POST":
        room_name = request.POST.get('room_name')

        rooms = room.objects.create(
            room_name=room_name
        )
    return render(request, 'team_post/lobby.html')

