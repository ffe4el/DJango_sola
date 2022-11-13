from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) #제목은 문자를 담는 필드로, 최대 30글자까지
    content = models.TextField() #내용은 문자열의 길이 제한이 없는 텍스트 필드
    head_image=models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #작성일은 월일시분초까지 기록할 수 있게 해주는 타임 필드
    update_at = models.DateTimeField(auto_now=True)
    # author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'
        #장고의 모델을 만들면 기본적으로 pk 필드가 만들어진다. pk는 각 레코드에 대한 고유값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
# Create your models here.
