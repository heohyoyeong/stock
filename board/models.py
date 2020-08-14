from django.db import models



class Post(models.Model):
    author = models.CharField("작성자", max_length=20)
    title = models.CharField("제목", max_length=100)
    contents = models.TextField('글 내용', max_length=2000)
    pub_date = models.DateTimeField('날짜',auto_now=True)


    def __str__(self):
        return self.contents