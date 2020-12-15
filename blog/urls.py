from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    PostCreateView,

    TagListView, 
    TagDetailView,
    TagDeleteView,
    TagUpdateView,
    TagCreateView,

    FormationListView, 
    FormationDetailView,
    FormationDeleteView,
    FormationUpdateView,
    FormationCreateView,

    LeconCreateView,
    LeconDetailView,
    LeconDeleteView,
    LeconUpdateView,

    CategoryListView,
    CategoryDetailView,
)

app_name = "blog"
urlpatterns = [
    path('blog/post/', PostListView.as_view(), name="list_all_post"),
    path('blog/post/create/', PostCreateView.as_view(), name="create_post"),
    path('blog/post/<slug:slug>/', PostDetailView.as_view(), name="detail_post"),
    path('blog/post/edit/<slug:slug>/', PostUpdateView.as_view(), name="edit_post"),
    path('blog/post/delete/<slug:slug>/', PostDeleteView.as_view(), name="delete_post"),

    path('blog/tag/', TagListView.as_view(), name="list_all_tag"),
    path('blog/tag/create/', TagCreateView.as_view(), name="create_tag"),
    path('blog/tag/<str:title>/', TagDetailView.as_view(), name="detail_tag"),
    path('blog/tag/edit/<str:title>/', TagUpdateView.as_view(), name="edit_tag"),
    path('blog/tag/delete/<str:title>/', TagDeleteView.as_view(), name="delete_tag"),


    path('blog/formation/', FormationListView.as_view(), name="list_all_formation"),
    path('blog/formation/create/', FormationCreateView.as_view(), name="create_formation"),
    path('blog/formation/<slug:slug>/', FormationDetailView.as_view(), name="detail_formation"),
    path('blog/formation/edit/<slug:slug>/', FormationUpdateView.as_view(), name="edit_formation"),
    path('blog/formation/delete/<slug:slug>/', FormationDeleteView.as_view(), name="delete_formation"),

    path('blog/lecon/create/', LeconCreateView.as_view(), name="create_lecon"),
    path('blog/lecon/<int:pk>/', LeconDetailView.as_view(), name="detail_lecon"),
    path('blog/lecon/edit/<int:pk>/', LeconUpdateView.as_view(), name="edit_lecon"),
    path('blog/lecon/delete/<int:pk>/', LeconDeleteView.as_view(), name="delete_lecon"),

    path('blog/category/', CategoryListView.as_view(), name="list_all_category"),
    path('blog/category/<str:title>/', CategoryDetailView.as_view(), name="detail_category"),
]
