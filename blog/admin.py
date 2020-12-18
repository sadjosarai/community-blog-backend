from django.contrib import admin
from .models import Tag, Category, Post, Formation, Lecon, Comment, ResponseComment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Lecon)
admin.site.register(Formation)
admin.site.register(Comment)
admin.site.register(ResponseComment)