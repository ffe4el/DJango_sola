from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class room(models.Model):
    room_name = models.CharField(null=True, max_length=30)

    def __str__(self):
        return f'{self.room_name}'


class talk(models.Model):
    writter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="talk", db_column="writter", null=True)
    massage = models.TextField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    roomname = models.ForeignKey(room, null=True, on_delete=models.CASCADE, db_column="roomname")
    # room_name = models.CharField(null=True, max_length=30)
    files = models.FileField(upload_to='team_post/files/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.writter.username}({self.pk}) :: {self.time_stamp}'

    def last_10_message(self):
        return talk.objects.order_by('time_stamp').all()[:10]

    # def get_absolute_url(self):
    #     return reverse('post:chat_room', kwargs={'pk': self.roomname})
