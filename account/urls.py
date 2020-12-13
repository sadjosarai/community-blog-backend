from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('account/', views.list_user, name="list_user"),
    path('account/<int:pk>/', views.detail_user, name="detail_user"),
    path('auth/', include('rest_auth.urls')),
    path('account/login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('account/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
