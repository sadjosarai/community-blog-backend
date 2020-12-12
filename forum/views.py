from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Comment, ResponseComment
from .serializers import ResponseCommentSerializer, CommentSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def list_comment(request, post_id):
    try:
        post = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'GET':
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)