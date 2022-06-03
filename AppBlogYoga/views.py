from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView     
from .models import Post
from .forms import PostForm, UpdateForm

#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering=['-fecha']

class DetailPost(DetailView):
    model = Post
    template_name = 'detailPost.html'

class CreatePost(CreateView):
    model = Post
    form_class= PostForm
    template_name = 'createPost.html'

class UpdatePost(UpdateView):
    model = Post
    form_class= UpdateForm
    template_name = 'updatePost.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url= reverse_lazy('home')
    
    
