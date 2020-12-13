from django.contrib import admin
from .models import Comment, ResponseComment
# Register your models here.

admin.site.register(Comment)
admin.site.register(ResponseComment)
