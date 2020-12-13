from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Comment, ResponseComment
from .serializers import ResponseCommentSerializer, CommentSerializer
from rest_framework import status
from rest_framework import generics

# Create your views here.

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
#    permission_classes = [IsAdminUser]


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

    
@api_view(['GET'])
def list_comment_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        comment = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)