from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('posts/', views.posts),
    path('', views.home),
]
