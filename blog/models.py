from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User ,related_name="categories", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    user = models.ForeignKey(User ,related_name="tags", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(User ,related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    banner = models.ImageField(upload_to='profiles/post/', null=True, blank=True)
    description = models.TextField(max_length=200, null=False)
    body = models.TextField()
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name="tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    