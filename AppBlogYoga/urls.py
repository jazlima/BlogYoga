from django.urls import path
#from . import views
from .views import HomeView, DetailPost, CreatePost

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detailPost'),
    path('createPost/', CreatePost.as_view(), name='createPost'),

]