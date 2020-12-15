from rest_framework.serializers import (
        HyperlinkedRelatedField,
        SerializerMethodField
    )
from rest_framework import serializers 
from .models import Post, Tag, Category, Formation, Lecon
from rest_framework.reverse import reverse
from django.http import HttpRequest

class FormationListSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    category = SerializerMethodField()

    class Meta:
        model = Formation
        fields = (
                    'user',
                    'title',
                    'category',
                    'description', 
                    'banner',
                    'publish_at',
                )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_category(self, obj):
        return str(obj.category.title)

class FormationDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    tag = SerializerMethodField()
    category = SerializerMethodField()
    summary = SerializerMethodField()
    
    class Meta:
        model = Formation
        fields = (
                    'user',
                    'title',
                    'slug',
                    'description', 
                    'banner', 
                    'category',
                    'publish_at',
                    'tag',
                    'prerequiste',
                    'objectif',
                    'summary'
                )

    def get_summary(self, obj):
        lecons = obj.lecon_formation.all()
        lecons_param = []
        for lecon in lecons:
            try :
                url = reverse("blog:detail_lecon", [lecon.pk])
            except Exception:
                url = None
            lecons_param.append({
                'url': url,
                'title' : lecon.title,
                'description': lecon.description
            })
        return lecons_param

    def get_user(self, obj):
        return str(obj.user.username)

    def get_tag(self, obj):
        tags = obj.tag.all()
        tag_title = []
        for tag in tags:
            tag_title.append(str(tag.title))
        return tag_title

    def get_category(self, obj):
        return str(obj.category.title)

class FormationCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Formation
        fields = (
                    'title',
                    'description', 
                    'banner', 
                    'category',
                    'tag',
                    'prerequiste',
                    'objectif',
                )

class FormationCreateUpdateSerializer(serializers.ModelSerializer):
    category = SerializerMethodField()
    tag = SerializerMethodField()
 
    class Meta:
        model = Formation
        fields = (
                    'title',
                    'description', 
                    'banner', 
                    'category',
                    'tag',
                    'prerequiste',
                    'objectif',
                )
    
    def get_tag(self, obj):
        tags = obj.tag.all()
        tag_title = []
        for tag in tags:
            tag_title.append(str(tag.title))
        return tag_title
    
    def get_category(self, obj):
        return str(obj.category.title)

class PostListSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    category = SerializerMethodField()

    class Meta:
        model = Post
        fields = (
                    'user',
                    'title',
                    'category',
                    'description', 
                    'banner',
                    'publish_at'
                )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_category(self, obj):
        return str(obj.category.title)

class PostDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    tag = SerializerMethodField()
    category = SerializerMethodField()
    
    class Meta:
        model = Post
        fields = (
                    'id',
                    'user',
                    'title',
                    'slug',
                    'description', 
                    'banner', 
                    'category',
                    'publish_at',
                    'body',
                    'tag',
                )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_tag(self, obj):
        tags = obj.tag.all()
        tag_title = []
        for tag in tags:
            tag_title.append(str(tag.title))
        return tag_title

    def get_category(self, obj):
        return str(obj.category.title)

class PostCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = (
                    'title',
                    'description', 
                    'banner', 
                    'category',
                    'body',
                    'tag',
                )

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    category = SerializerMethodField()
    tag = SerializerMethodField()
 
    class Meta:
        model = Post
        fields = (
                    'title',
                    'description',
                    'banner',
                    'category',
                    'body',
                    'tag',
                )
    
    def get_tag(self, obj):
        tags = obj.tag.all()
        tag_title = []
        for tag in tags:
            tag_title.append(str(tag.title))
        return tag_title
    
    def get_category(self, obj):
        return str(obj.category.title)

class CategoryListSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Category
        fields = (
                    'user',
                    'title',
                    'description'
                )

    def get_user(self, obj):
        return str(obj.user.username)

class CategoryDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    posts = SerializerMethodField()

    class Meta:
        model = Category
        fields = (
                    'user',
                    'title',
                    'description',
                    'posts',
                    'created_at',
                )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_posts(self, obj):
        posts = obj.posts_category.all()
        posts_slug = []
        for post in posts:
            posts_slug.append(str(post.slug))
        return posts_slug

class TagListSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
                    'user',
                    'title'
                )

    def get_user(self, obj):
        return str(obj.user.username)

class TagDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    posts = SerializerMethodField()

    class Meta:
        model = Tag
        fields = (
                    'user',
                    'title',
                    'posts',
                    'created_at'
                )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_posts(self, obj):
        posts = obj.posts_tag.all()
        posts_slug = []
        for post in posts:
            posts_slug.append(str(post.slug))
        return posts_slug

class TagCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
                    'title',
                    'created_at',
                )

class LeconDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = (
                    'title',
                    'description', 
                    'banner',
                    'body',
                    'update_at',
                )

class LeconCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecon
        fields = (
                    'title',
                    'description', 
                    'banner',
                    'body',
                    'formation',
                    'updated_at',
                )
