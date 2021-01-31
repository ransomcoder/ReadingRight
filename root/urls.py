from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='access_token'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
