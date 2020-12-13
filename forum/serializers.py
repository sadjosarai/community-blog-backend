from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, ResponseComment
from account.serializers import UserSerializer


class ResponseCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseComment
        fields = ('id', 'created_at', 'body')


class CommentSerializer(serializers.ModelSerializer):

    responses = ResponseCommentSerializer(many=True, read_only=True)
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'body', 'user', 'post', 'responses')