from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog_home'),
    path('about/', views.about, name='blog_about'),
]