from django.urls import path
from .import views

urlpatterns = [
    path('forums/comment/user/<int:pk>/', views.list_comment_user),
    path('forums/comment/post/<int:pk>/', views.list_comment_post),
    path('forums/comment/response/<int:pk>/', views.list_response_comment),
]