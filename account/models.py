from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='profiles/users/', null=True, blank=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'