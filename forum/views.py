from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Comment, ResponseComment
from .serializers import ResponseCommentSerializer, CommentSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from blog.models import Post
from .models import Comment

# Create your views here.

@api_view(['GET'])
def list_comment_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        comment = Comment.objects.filter(user=user)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def list_comment_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        comment = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

#vérifier si le user est connecté
    elif request.method == 'POST':
        if request.user.is_authenticated:
            data = request.data
            try:
                user = User.objects.get(pk=data["user"])
            except User.DoesNotExist:
                return HttpResponse(status=404)

            comment = Comment.objects.create(user=user, post=post, body=data['body'])
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        return Response({"error": "please log you"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'POST'])
def list_response_comment(request, pk):

    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        response = ResponseComment.objects.filter(comment=comment)
        serializer = ResponseCommentSerializer(response, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            data = request.data
            try:
                user = User.objects.get(pk=data["user"])
            except User.DoesNotExist:
                return HttpResponse(status=404)

            response = ResponseComment.objects.create(user=user, comment=comment, body=data['body'])
            response.save()
            serializer=ResponseCommentSerializer(response)
            return Response(serializer.data)
        return Response({"error": "please log you"}, status=status.HTTP_400_BAD_REQUEST)
