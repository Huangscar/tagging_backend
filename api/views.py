from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tag.models import *
from django.db.models import Q
from api.serializers.tagpic_serializer import *
from api.serializers.user_serializer import *
from api.serializers.episode_serializer import *
from django.contrib.auth.hashers import make_password, check_password

class TagingPic(APIView):
    def get(self, request, format=None):
        pic_id = int(request.data['id'])
        tag_pic = TagPic.objects.get(id=pic_id)
        tag_pic_serializer = TagPicSerializer(tag_pic)
        res = {
            'num': len(tag_pic_serializer.data),
            'data': tag_pic_serializer.data
        }
        return Response(res, status=status.HTTP_200_OK)

class TaggingPicP(APIView):
    def get(self, request, format=None):
        try:
            data = request.data
            print(data)
            id = int(data['id'])
            tag_pic = TagPic.objects.get(id=id)
            if data['change']:
                data['name'] = data['result']
            result = TagPicSerializer(tag_pic, data=data)
            if result.is_valid():
                tag_pic_r = result.save()
                book_id = tag_pic.book_id
                episode = tag_pic.episode
                next_pic = TagPic.objects.filter(Q(book_id=book_id) & Q(episode=episode) & Q(tag_num=0)).order_by('id')
                if next_pic.count() != 0:
                    next_serializer = TagPicSerializer(next_pic.first())
                    next_result = next_serializer.data
                else:
                    next_result = ""
                res = {
                    "info": "修改成功",
                    "data": result.data,
                    "next_pic": next_result
                }
                return Response(res, status=status.HTTP_200_OK)
            else:
                print("not valid")
                return Response(status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return Response(status.HTTP_400_BAD_REQUEST)

class EpisodePic(APIView):
    def get(self, request, format=None):
        eid = int(request.query_params['id'])
        pic = TagPic.objects.filter(episode__id=eid)
        pic_serializer = TagPicSerializer(pic, many=True)
        res = {
            "num": len(pic_serializer.data),
            "data": pic_serializer.data
        }
        return Response(res, status=status.HTTP_200_OK)

class Book(APIView):
    def get(self, request, format=None):
        book_id = int(request.query_params['book_id'])
        episode = Episode.objects.filter(book_id=book_id)
        episode_serializer = EpisodeSerializer(episode, many=True)
        res = {
            "num": len(episode_serializer.data),
            "data": episode_serializer.data
        }

        return Response(res, status=status.HTTP_200_OK)

class Login(APIView):
    def get(self, request, format=None):
        userdata = request.data
        print(userdata)
        username = userdata['username']
        user = User.objects.get(username=username)
        password = user.password
        if check_password(userdata['password'], password):
            user_serializer = UserSerializer(user)
            res = {
                "info": "登陆成功",
                "data": user_serializer.data
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

class Resister(APIView):
    def get(self, request, format=None):
        user_data = request.data
        print(user_data)
        user = User.objects.filter(username=user_data['username'])
        if user.count() != 0:
            res = {"该用户名已被注册"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        user_data['password_write'] = make_password(user_data['password'], salt=False, hasher='default')
        data = UserSerializer(data=user_data)
        if data.is_valid():
            data.save()
            res = {
                "info": "注册成功",
                "data": data.data
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)




