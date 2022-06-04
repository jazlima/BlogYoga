from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView     
from .models import Category, Post
from .forms import PostForm, UpdateForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering=['-fecha']

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        contexto=super(HomeView, self).get_context_data(*args, **kwargs)
        contexto['cat_menu']=cat_menu
        return contexto 

class DetailPost(DetailView):
    model = Post
    template_name = 'detailPost.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        contexto=super(DetailPost, self).get_context_data(*args, **kwargs)
        contexto['cat_menu']=cat_menu
        return contexto 

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

def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
    
    
    
    
