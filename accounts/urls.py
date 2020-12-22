from django.urls import path, include
from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('rest_auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/all-profiles/',UserProfileListCreateView.as_view(),name="all-profiles"),
    path("auth/profile/<int:pk>/",UserProfileDetailView.as_view(),name="profile"),
]