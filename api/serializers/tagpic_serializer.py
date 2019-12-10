#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 11:34 上午
# @Author  : huangscar
# @Site    : 
# @File    : tagpic_serializer.py
# @Software: PyCharm

from rest_framework import serializers
from tag.models import *
from django.db.models import Q

class TagPicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.IntegerField(required=False)
    episode = serializers.SerializerMethodField(required=False)
    pos = serializers.SerializerMethodField(required=False)
    name = serializers.CharField(required=False)
    pic_index = serializers.IntegerField(required=False)
    url = serializers.SerializerMethodField(required=False)
    tag_user = serializers.SerializerMethodField(required=False)
    if_mark = serializers.SerializerMethodField(required=False)

    result = serializers.CharField(write_only=True)
    change = serializers.BooleanField(write_only=True)
    uid = serializers.IntegerField(write_only=True)

    def get_pos(self, obj):
        pos_result = obj.pos.split(', ')
        pos_result[0] = pos_result[0][1:]
        pos_result[3] = pos_result[3][:-1]
        pos_result_num = []
        for pos in pos_result:
            pos_result_num.append(int(pos))
        return pos_result_num

    def get_url(self, obj):
        book_id = obj.book_id
        episode = obj.episode
        episode_str = 'EP%02d_drop_similar' % episode.episode_index
        return '/static/' + str(book_id) + '/' + episode_str + '/' + obj.pic_url

    def get_tag_user(self, obj):
        users = obj.users.all()
        if users.count() == 0:
            return ''
        else:
            user = users.order_by('-id').first()
            return user.username

    def get_if_mark(self, obj):
        if int(obj.tag_num) == 0:
            return False
        else:
            return True

    def get_episode(self, obj):
        return obj.episode.id


    def update(self, instance, validated_data):
        if not validated_data['change']:
            instance.name = validated_data['result']
        instance.tag_num = instance.tag_num+1
        tag_user = User.objects.filter(id=validated_data['uid'])
        instance.users.add(*tag_user)
        instance.time = timezone.now()
        last_work_str = str(instance.id)
        tag_user_one = tag_user.first()
        tag_user_one.last_work = last_work_str
        tag_user_one.save()
        instance.save()
        return instance
