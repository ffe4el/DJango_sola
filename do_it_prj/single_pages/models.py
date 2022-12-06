from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=30) #제목은 문자를 담는 필드로, 최대 30글자까지
    head_image = models.ImageField(upload_to='single_pages/images/avatar', blank=True)
    hook_text = models.CharField(max_length=50)
    port1_title = models.CharField(max_length=30, default='')
    port1 = models.TextField(blank=True) #내용은 문자열의 길이 제한이 없는 텍스트 필드
    port1_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port2_title = models.CharField(max_length=30, default='')
    port2 = models.TextField(blank=True)
    port2_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port3_title = models.CharField(max_length=30, default='')
    port3 = models.TextField(blank=True)
    port3_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port4_title = models.CharField(max_length=30, default='')
    port4 = models.TextField(blank=True)
    port4_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port5_title = models.CharField(max_length=30, default='')
    port5 = models.TextField(blank=True)
    port5_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port6_title = models.CharField(max_length=30, default='')
    port6 = models.TextField(blank=True)
    port6_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    about_me = models.TextField(max_length=100, default='')
    profile_image = models.ImageField(upload_to='single_pages/static/single_pages/bootstrap/asseets/img/avatar1/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일은 월일시분초까지 기록할 수 있게 해주는 타임 필드
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} :: {self.name} :: Portfolio'

    def get_absolute_url(self):
        return f'/post/{self.pk}/'
# Create your models here.
