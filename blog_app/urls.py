from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('post/', views.post, name='blog_post'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='post-delete'),
    path('post/new', views.PostCreate.as_view(), name='post-create')
]