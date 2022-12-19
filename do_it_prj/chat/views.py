from django.shortcuts import render, redirect
from . import models
from .models import Message

import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse


# def room(request, room_name):
#     Messages = Message.objects.all()
#     if request.method == "POST":
#         # Fetching the form data
#         fileTitle = request.POST["fileTitle"]
#         uploadedFile = request.FILES["uploadedFile"]
#
#         # Saving the information in the database
#         document = models.Document(
#             title=fileTitle,
#             uploadedFile=uploadedFile
#         )
#         document.save()
#
#     documents = models.Document.objects.all()
#
#     return render(request, "chat/room.html", context={
#         "files": documents,
#         "room_name": room_name,
#     })


def index(request):
    return render(request, "chat/index.html")


def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "chat/room.html", context={
        "files": documents,
    })


def room(request, room_name):
    Messages = Message.objects.all()
    if request.method == "POST":
        content = request.POST['content']

        author = request.user


        Messages = Message.objects.create(
            content=content,
            # timestamp=timestamp,
            author=author
        )

        Messages.save()

    return render(request, 'chat/room.html', context={
        "Messages": Messages,
        "room_name": room_name,
    })

# def downloadFile(request):
# file_path = os.path.abspath("media/result/")
# file_name = os.path.basename("media/result/급여지급현황.xlsx")
# fs = FileSystemStorage(file_path)
# response = FileResponse(fs.open(file_name, 'rb'),
#                         content_type='application/vnd.ms-excel')
# response['Content-Disposition'] = 'attachment; filename="salary.xlsx"'
#
# return response
# path = request.GET['path']
# file_path = os.path.join(settings.MEDIA_ROOT, path)
#
# if os.path.exists(file_path):
#     binary_file = open(file_path, 'rb')
#     response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
#     response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
#     return response
# else:
#     message = '알 수 없는 오류가 발행하였습니다.'
#     return HttpResponse("<script>alert('" + message + "');history.back()'</script>")
