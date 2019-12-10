#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 1:34 上午
# @Author  : huangscar
# @Site    : 
# @File    : episode_serializer.py
# @Software: PyCharm

from rest_framework import serializers
from tag.models import *
from django.db.models import Q

class EpisodeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.IntegerField()
    name = serializers.CharField()
    total_num = serializers.SerializerMethodField(required=False)
    complete_num = serializers.SerializerMethodField(required=False)
    last = serializers.SerializerMethodField(required=False)

    def get_total_num(self, obj):
        tag_pic = TagPic.objects.filter(episode__id=obj.id)
        return len(tag_pic)

    def get_complete_num(self, obj):
        tag_pics = TagPic.objects.filter(Q(episode__id=obj.id) & ~Q(tag_num=0))
        return len(tag_pics)

    def get_last(self, obj):
        tag_pic = TagPic.objects.filter(Q(episode__id=obj.id) & ~Q(tag_num=0))
        if tag_pic.count() > 0:
            user = tag_pic.first().users.first()
            return user.username
        else:
            return ""







