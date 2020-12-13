from django.urls import path
from .import views

urlpatterns = [
    path('forums/comment/', views.CommentList.as_view()),

    path('forums/comment/user/<int:pk>/', views.list_comment_user),
    path('forums/comment/post/<int:pk>/', views.list_comment_post)
]