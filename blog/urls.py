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
    path('post/', PostListView.as_view(), name="list_all_post"),
    path('post/create/', PostCreateView.as_view(), name="create_post"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="detail_post"),
    path('post/edit/<slug:slug>/', PostUpdateView.as_view(), name="edit_post"),
    path('post/delete/<slug:slug>/', PostDeleteView.as_view(), name="delete_post"),

    path('tag/', TagListView.as_view(), name="list_all_tag"),
    path('tag/create/', TagCreateView.as_view(), name="create_tag"),
    path('tag/<str:title>/', TagDetailView.as_view(), name="detail_tag"),
    path('tag/edit/<str:title>/', TagUpdateView.as_view(), name="edit_tag"),
    path('tag/delete/<str:title>/', TagDeleteView.as_view(), name="delete_tag"),


    path('formation/', FormationListView.as_view(), name="list_all_formation"),
    path('formation/create/', FormationCreateView.as_view(), name="create_formation"),
    path('formation/<slug:slug>/', FormationDetailView.as_view(), name="detail_formation"),
    path('formation/edit/<slug:slug>/', FormationUpdateView.as_view(), name="edit_formation"),
    path('formation/delete/<slug:slug>/', FormationDeleteView.as_view(), name="delete_formation"),

    path('lecon/create/', LeconCreateView.as_view(), name="create_lecon"),
    path('lecon/<int:pk>/', LeconDetailView.as_view(), name="detail_lecon"),
    path('lecon/edit/<int:pk>/', LeconUpdateView.as_view(), name="edit_lecon"),
    path('lecon/delete/<int:pk>/', LeconDeleteView.as_view(), name="delete_lecon"),

    path('category/', CategoryListView.as_view(), name="list_all_category"),
    path('category/<str:title>/', CategoryDetailView.as_view(), name="detail_category"),
]
