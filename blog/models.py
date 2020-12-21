from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User ,related_name="categories", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)
    description = models.TextField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('category-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Tag(models.Model):
    user = models.ForeignKey(User ,related_name="user_tags", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('tag-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    user = models.ForeignKey(User ,related_name="posts_user", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)
    banner = models.URLField(max_length=200, blank=True)
    description = models.TextField(max_length=200, blank=False)
    body = models.TextField(blank=False)
    category = models.ForeignKey(Category, related_name="posts_category", on_delete=models.CASCADE, blank=False)
    tag = models.ManyToManyField(Tag, related_name="posts_tag", blank=True)
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft'
                            )

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Formation(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    user = models.ForeignKey(User ,related_name="formation_user", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)
    banner = models.URLField(max_length=200, blank=True)
    description = models.TextField(max_length=200, blank=False)
    category = models.ForeignKey(Category, related_name="formation_category", on_delete=models.CASCADE, blank=False)
    tag = models.ManyToManyField(Tag, related_name="formation_tag", blank=True)
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prerequiste = models.TextField(max_length=200, blank=True)
    objectif = models.TextField(max_length=200, blank=False)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft'
                            )

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('formation-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class  Lecon(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200, unique=True)
    banner = models.URLField(max_length=200, blank=True)
    durate = models.TimeField(auto_now=False, auto_now_add=False)
    position = models.IntegerField()
    body = models.TextField(blank=False)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="summary", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        kwargs = {'pk': self.pk}
        return reverse('blog:detail_lecon', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class ResponseComment(models.Model):
    user = models.ForeignKey(User, related_name="userresponse", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="responses", on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)