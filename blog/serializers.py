from rest_framework.serializers import (
        HyperlinkedRelatedField,
        SerializerMethodField
    )
from rest_framework import serializers 
from .models import Post, Tag, Category, Formation, Lecon, Comment, ResponseComment
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
    lecon = SerializerMethodField()
    summary = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog:detail_lecon',
        lookup_field = 'pk',
        lookup_url_kwarg = 'pk'
    )
    
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
                    'summary',
                    'lecon',
                )

    def get_lecon(self, obj):
        lecons = obj.summary.all()
        lecons_param = []
        for i in range(len(lecons)):
            item = {
                "title": lecons[i].title,
                "link": summary[i]
            }
            lecons_param.append(item)
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
    user_id = SerializerMethodField()
    
    class Meta:
        model = Post
        fields = (
                    'id',
                    'user_id',
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

    def get_user_id(self, obj):
        return int(obj.user.pk)


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
        posts_data = []
        for post in posts:
            item = {
                    'id': post.pk,
                    'user': post.user.username,
                    'title': post.title,
                    'slug': post.slug,
                    'description':post.description, 
                    'banner':post.banner,
                    'publish_at':post.publish_at,
                }
            posts_data.append(item)
        return posts_data

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

class PostCommentDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    comment = SerializerMethodField()
    
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'slug',
            'description', 
            'banner', 
            'publish_at',
            'body', 
            'comment',
        )
    
    def get_user(self, obj):
        return str(obj.user.username)
    
    def get_comment(self, obj):
        comments = obj.comments.all()
        comments_data = []
        for comment in comments:
            responses = comment.responses.all()
            responses_data = []
            for response in responses:
                itemres = {
                        'name': response.user.username, 
                        'created_at': response.created_at,
                        'body': response.body
                }
                responses_data.append(itemres)
            item = {
                        'name': comment.user.username, 
                        'created_at': comment.created_at,
                        'body': comment.body,
                        'response': responses_data,
                    }
            comments_data.append(item)
        return comments_data

class CommentCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comment
        fields = (
                    'user',
                    'post',
                    'created_at',
                    'body',
                )

class ResponseCommentCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ResponseComment
        fields = (
                    'created_at',
                    'user',
                    'comment',
                    'body',
                )

class CommentDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    post_name = SerializerMethodField()
    post_slug = SerializerMethodField() 
    response = SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
                    'user',
                    'post_name',
                    'post_slug',
                    'created_at',
                    'body',
                    'response',
                )
    def get_user(self, obj):
        return str(obj.user.username)

    def get_post_name(self, obj):
       return str(obj.post.title)

    def get_post_slug(self, obj):
       return str(obj.post.slug)

    def get_response(self, obj):
        responses = obj.responses.all()
        responses_data = []
        for response in responses:
            item = {
                    'name': response.user.username, 
                    'created_at': response.created_at,
                    'body': response.body
            }
            responses_data.append(item)
        return responses_data

