from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey("app.Model", related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ResponseComment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="responses", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.models.DateField(auto_now_add=True)