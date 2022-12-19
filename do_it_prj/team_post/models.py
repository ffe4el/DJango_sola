from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.

class room(models.Model):
    roomname = models.CharField(null=True, max_length=30, db_column="room_name")

    def __str__(self):
        return f'{self.roomname}'

    def get_absolute_url(self):
        return f'/team_post/{self.roomname}/'

class talk(models.Model):
    writter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="talk", db_column="writter", null=True)
    massage = models.TextField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    roomname = models.ForeignKey(room, null=True, related_name="talk_room", on_delete=models.CASCADE, db_column="roomname")
    # room_name = models.CharField(null=True, max_length=30)
    files = models.FileField(upload_to='team_post/files/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        if self.writter is None:
            return f'None({self.pk}) :: {self.time_stamp}'
        return f'{self.writter.username}({self.pk}) :: {self.time_stamp}'

    def last_10_message(self):
        return talk.objects.order_by('time_stamp').all()[:10]

    def get_file_name(self):
        return os.path.basename(self.files.name)

    # def get_absolute_url(self):
    #     return f'/team_post/{self.roomname}/'

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
