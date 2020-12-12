from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, ResponseComment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'body')

class ResponseCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseComment
        fields = ('id', 'created_at', 'body')