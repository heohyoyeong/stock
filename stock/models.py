from django.db import models
import datetime


class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='아이디')
    password = models.CharField(max_length=30, verbose_name='패스워드')
    registered_dttm = models.DateTimeField(auto_now_add = True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'test_user'


class stockname(models.Model):
    stock_text=models.ForeignKey(User,on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=30)
    stock_code = models.IntegerField()
    stock_money = models.IntegerField()

    def __str__(self):
        return self.stock_name


class stockhistory(models.Model):
    history_text=models.ForeignKey(User,on_delete=models.CASCADE)
    history_name = models.CharField(max_length=30)
    history_code = models.IntegerField()
    history_money = models.IntegerField()
    history_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.history_name

class Chat(models.Model):
    chat_text=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=30)