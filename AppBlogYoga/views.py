from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView     
from .models import Category, Post
from .forms import PostForm, UpdateForm


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

class CreateCategory(CreateView):
    model = Category
    template_name = 'createCategory.html'
    fields='__all__'

def CategoryView(request, cat):
    category_posts=Post.objects.filter(categoria=cat)
    return render(request, 'categories.html', {'cat':cat.title(), 'category_posts':category_posts})
    
    
    
    
