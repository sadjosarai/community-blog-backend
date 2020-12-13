from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Category, Tag, Post
from .serializers import CategorySerializer, TagSerializer, PostSerializer
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-publish')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            try:
                category = Category.objects.get(id=data['category'])
            except Category.DoesNotExist:
                return HttpResponse(status=404)

            tags = []
            for tag in data['tag']:
                try:
                    tags.append(Tag.objects.get(id=tag))
                except Tag.DoesNotExist:
                    return HttpResponse(status=404)

            data = request.data
            post.title = data["title"]
            post.description = data["description"]
            post.body = data["body"]
            post.banner = data["banner"]
            post.tag.set(tags)
            post.category = category

            post.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def post_list_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    posts = Post.objects.filter(user=user).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_list_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    posts = Post.objects.filter(category=category).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_list_tag(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    posts = Post.objects.filter(tag=tag).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all().order_by('-created_at')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(data=request.data)
        if request.user == category.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
      
    elif request.method == 'DELETE':
        category.delete()
        return Response( status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def category_list_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    categories = Category.objects.filter(user=user).order_by('-created_at')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all().order_by('-created_at')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tag.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def tag_list_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    tags = Tag.objects.filter(user=user).order_by('-created_at')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tag_list_article(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    
    tags = post.tag.all()
    print (tags)           
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)
