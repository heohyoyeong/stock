from django.db import models
from django.utils import timezone
now = timezone.localtime()



class Post(models.Model):
    author = models.CharField("작성자", max_length=20, blank=True)
    title = models.CharField("제목", max_length=100)
    contents = models.TextField('글 내용', max_length=2000)
    pub_date = models.DateTimeField('날짜',auto_now=True)
    maching_code = models.CharField("작성게시판코드명", max_length=100)
    stock_name = models.CharField("작성게시판", max_length=100, blank=True)



    def __str__(self):
        return self.contents



class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
