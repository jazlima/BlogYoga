from django.urls import path
from .views import HomeView, DetailPost, CreatePost, UpdatePost, DeletePost, CreateCategory, CategoryView, CategoryListView, LikeView, AddComment, about

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detailPost'),
    path('createPost/', CreatePost.as_view(), name='createPost'),
    path('updatePost/<int:pk>/', UpdatePost.as_view(), name='updatePost'),
    path('deletePost/<int:pk>/', DeletePost.as_view(), name='deletePost'),

    path('createCategory/', CreateCategory.as_view(), name='createCategory'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),

    path('like/<int:pk>/', LikeView, name='like_post'),

    path('post/<int:pk>/comment', AddComment.as_view(), name='addComment'),

    path('about/', about, name="about"),

]