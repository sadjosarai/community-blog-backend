from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    CATEGORY_CHOICES = (
        ('mobile', 'Mobile'),
        ('securite', 'Securite'),
        ('web', 'Web'),
        ('machinelearning', 'MachineLearning'),
        ('datascience', 'DataScience'),
    )
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField(max_length=255,unique_for_date='publish')
    publish = models.DateField(default = timezone.now)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES, default = 'draft')
    category = models.CharField(max_length=255, choices = CATEGORY_CHOICES, default='web')
    
    
    def __str__(self):
        return self.title
