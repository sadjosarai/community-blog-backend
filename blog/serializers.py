
from account.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Tag, Post

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'description')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'description', 'body', 'category', 'tag', 'updated_at', 'banner')
        depth = 1
        read_only_fields = ['user']