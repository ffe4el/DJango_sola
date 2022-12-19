from django.shortcuts import render, redirect, get_object_or_404
from .models import talk, room
from datetime import datetime
from django.contrib.auth import get_user_model


# Create your views here.
def chat_room(request, room_name):
    all_talks = talk.objects.all()
    room_name1 = room.objects.get(roomname=room_name)
    talks = talk.objects.filter(roomname=room_name1)
    chat_user = []
    for t in talks:
        if not t.writter.username in chat_user:
            chat_user.append(t.writter.username)

    room_list = []
    for x in all_talks:
        if str(x.writter) == str(request.user):
            if not x.roomname in room_list:
                room_list.append(x.roomname)

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
            roomname=room_name1

        )

        return redirect('chat_room', room_name)

    return render(request, 'team_post/chat_room.html', context={
        "talks": talks,
        "room_name": room_name,
        "chat_user": chat_user,
        "room_list": room_list
    })


def lobby(request):
    talks = talk.objects.all()
    rooms = room.objects.all()
    room_list = []
    for x in talks:
        if str(x.writter) == str(request.user):
            if not x.roomname in room_list:
                room_list.append(x.roomname)

    if request.method == "POST":
        room_name = request.POST['room_name']

        rooms = room.objects.create(
            roomname=room_name
        )
        return redirect('lobby')

    return render(request, 'team_post/lobby.html',
                  context={
                      'rooms': rooms,
                      'talks': talks,
                      "room_list": room_list
                  })
