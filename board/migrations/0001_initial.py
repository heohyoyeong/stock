# Generated by Django 3.0.8 on 2020-08-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='작성자')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('contents', models.TextField(max_length=2000, verbose_name='글 내용')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='날짜')),
            ],
        ),
    ]
