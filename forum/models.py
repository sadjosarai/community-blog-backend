from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="usercomments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class ResponseComment(models.Model):
    user = models.ForeignKey(User, related_name="userresponse", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="responses", on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)