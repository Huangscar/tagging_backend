from django.db import models

# Create your models here.
from typing import Tuple
from django.db import models
from django.utils import timezone

BOOK_ID = ((0, '红楼梦'), (1, '西游记'), (2, '水浒传'), (3, '三国演义'))
USER_STATUS = ((1, '未登录'), (2, '已登陆'))

class TagPic(models.Model):
    book_id = models.IntegerField(verbose_name="书本id", choices=BOOK_ID, default=3)
    episode = models.ForeignKey('Episode', on_delete=models.CASCADE, to_field='id', verbose_name='集')
    pic_url = models.TextField(verbose_name='图片名称', default='')
    pic_index = models.IntegerField(verbose_name='图片序号', default=0)
    pos = models.TextField(verbose_name='红框位置', default='')
    name = models.TextField(verbose_name='名称', default='')
    tag_num = models.IntegerField(verbose_name='标记次数', default=0)
    users = models.ManyToManyField('User', verbose_name='标记用户')
    time = models.DateTimeField(verbose_name='标记时间', default=timezone.now())

class Episode(models.Model):
    book_id = models.IntegerField(verbose_name="书本id", choices=BOOK_ID, default=3)
    name = models.TextField(verbose_name="集数名称", default='集')
    episode_index = models.IntegerField(verbose_name='集数', default=1)

class User(models.Model):
    username = models.TextField(verbose_name='用户名', default='')
    password = models.TextField(verbose_name='密码', default='')
    last_work = models.TextField(verbose_name='最后录到的记录', default='')
    status = models.IntegerField(verbose_name='用户登陆状态', default=1)


