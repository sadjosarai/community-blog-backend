from django.urls import path
from .import views

urlpatterns = [
    path('blog/article/', views.blog_list),
    path('blog/article/<int:pk>/', views.blog_detail),
]