from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)#타이틀에 이거저장
    pub_date = models.DateTimeField('date puublished')#타이틀에 시간저장
    body = models.TextField()

    def __str__(self):#이거쓰면 제목이보임
        return self.title

    def summary(self):
        return self.body[:100] 

# Create your models here.
