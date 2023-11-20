from rest_framework import serializers
from post.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
