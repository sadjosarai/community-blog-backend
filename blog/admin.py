from django.contrib import admin
from .views import Tag, Category, Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)