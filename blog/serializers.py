from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(ModelSerializer):

    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    class Meta: 
        model = Article
        fields = ['id', 'title', 'slug', 'author', 'body', 'category']