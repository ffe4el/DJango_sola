from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


class Post(models.Model):
    name = models.CharField(max_length=30) #제목은 문자를 담는 필드로, 최대 30글자까지
    head_image = models.ImageField(upload_to='single_pages/images/avatar', blank=True)
    hook_text = models.CharField(max_length=50)
    port1_title = models.CharField(max_length=30, default='')
    port1 = MarkdownxField()
    port1_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port2_title = models.CharField(max_length=30, default='')
    port2 = MarkdownxField()
    port2_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port3_title = models.CharField(max_length=30, default='')
    port3 = MarkdownxField()
    port3_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port4_title = models.CharField(max_length=30, default='')
    port4 = MarkdownxField()
    port4_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port5_title = models.CharField(max_length=30, default='')
    port5 = MarkdownxField()
    port5_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    port6_title = models.CharField(max_length=30, default='')
    port6 = MarkdownxField()
    port6_img = models.ImageField(upload_to='single_pages/images/portfolio', blank=True)
    about_me = models.TextField(max_length=100, default='')
    profile_image = models.ImageField(upload_to='single_pages/static/single_pages/bootstrap/asseets/img/avatar1/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일은 월일시분초까지 기록할 수 있게 해주는 타임 필드
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} :: {self.name} :: Portfolio'

    def get_absolute_url(self):
        return f'/post/{self.pk}/'

    def get_port1_markdown(self):
        return markdown(self.port1)

    def get_port2_markdown(self):
        return markdown(self.port2)

    def get_port3_markdown(self):
        return markdown(self.port3)

    def get_port4_markdown(self):
        return markdown(self.port4)

    def get_port5_markdown(self):
        return markdown(self.port5)

    def get_port6_markdown(self):
        return markdown(self.port6)
# Create your models here.
