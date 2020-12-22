from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=200, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    github = models.URLField(max_length=200, blank=True)
    linked_in = models.URLField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_redactor = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.user.username