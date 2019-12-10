#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 2:25 下午
# @Author  : huangscar
# @Site    : 
# @File    : user_serializer.py
# @Software: PyCharm

from rest_framework import serializers
from tag.models import *

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password_write = serializers.CharField(write_only=True)
    last_work = serializers.CharField(required=False)


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password_write']
        )
        return user

