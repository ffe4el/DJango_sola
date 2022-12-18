from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message", db_column="author")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_message(self):
        return Message.objects.order_by('-timestamp').all()[:10]


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="result/%Y/%m/%d/", blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


