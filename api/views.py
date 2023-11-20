from django.shortcuts import render
from api.serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from post.models import Post
from rest_framework import viewsets

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
