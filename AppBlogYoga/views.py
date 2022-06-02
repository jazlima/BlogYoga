from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView  
from .models import Post

#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class DetailPost(DetailView):
    model = Post
    template_name = 'detailPost.html'

class CreatePost(CreateView):
    model = Post
    template_name = 'createPost.html'
    fields = ['titulo', 'subtitulo', 'autor', 'cuerpo', 'imagen']
