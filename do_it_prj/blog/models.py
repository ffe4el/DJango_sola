from django.db import models
from django.contrib.auth.models import User
import os
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=30) #제목은 문자를 담는 필드로, 최대 30글자까지
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()
    head_image=models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #작성일은 월일시분초까지 기록할 수 있게 해주는 타임 필드
    update_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #CASCADE는 작성자가 데이터베이스에서 삭제되었을때 이 포스트도 같이 삭제한다라는 의미.
                                                                #SET_NULL은 작성자가 데이터베이스에서 삭제되었을때 이 포스트의 작성자명을 null값으로 둔다는 의미.
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
        #장고의 모델을 만들면 기본적으로 pk 필드가 만들어진다. pk는 각 레코드에 대한 고유값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] #확장자 찾기

    def get_content_markdown(self):
        return markdown(self.content)
# Create your models here.

