from django.urls import path
from .views import HomeView, DetailPost, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detailPost'),
    path('createPost/', CreatePost.as_view(), name='createPost'),
    path('updatePost/<int:pk>/', UpdatePost.as_view(), name='updatePost'),
    path('deletePost/<int:pk>/', DeletePost.as_view(), name='deletePost'),

]