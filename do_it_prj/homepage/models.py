from django.db import models

from django.db import models

from django.contrib.auth.models import User

class Topic(models.Model):
    message = models.TextField(max_length=5000,blank=False,default='')
    subject = models.CharField(max_length=255, blank=False,default='')
    last_updated =  models.DateField(auto_now_add=True, null=True)
    writter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'[{self.pk}] {self.subject}'

class Reply(models.Model):
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, null=True, related_name='posts',on_delete=models.CASCADE)
    updated_at = models.DateField(null = True)
    updated_by=  models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)
    def __str__(self):
        return f'[{self.pk}] {self.subject}'


class Account(models.Model):
    name = models.TextField(max_length=20)
    email = models.TextField(max_length=20)
    last_updated = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)

# Create your models here.
