from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer, RegisterSerializer, MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['GET', 'POST'])
def list_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if request.user.pk == pk:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response([{"error": "you dont have permission to change this count"}], status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if request.user.pk == pk or request.user.is_superuser:
            user.delete()
            return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
        return Response([{"error": "you dont have permission to delete this count"}], status = status.HTTP_400_BAD_REQUEST)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer