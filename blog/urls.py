from django.urls import path
from .import views

urlpatterns = [
    path('blog/article/', views.post_list),
    path('blog/article/<int:pk>/', views.post_detail),
    path('blog/article/user/<int:pk>/', views.post_list_user),
    path('blog/article/category/<int:pk>/', views.post_list_category),
    path('blog/article/tag/<int:pk>/', views.post_list_tag),

    path('blog/category/', views.category_list),
    path('blog/category/<int:pk>/', views.category_detail),
    path('blog/category/user/<int:pk>/', views.category_list_user),

    path('blog/tag/', views.tag_list),
    path('blog/tag/<int:pk>/', views.tag_detail),
    path('blog/tag/user/<int:pk>/', views.tag_list_user),

    path('blog/tag/article/<int:pk>/', views.tag_list_article),
]