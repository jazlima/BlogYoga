from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView     
from .models import Category, Post
from .forms import PostForm, UpdateForm
from django.http import HttpResponseRedirect


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

        var=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=var.total_likes()

        liked=False
        if var.likes.filter(id=self.request.user.id).exists():
            liked=True

        contexto['cat_menu']=cat_menu
        contexto['total_likes']=total_likes
        contexto['liked']=liked
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

def LikeView(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
        
    return HttpResponseRedirect(reverse('detailPost', args=[str(pk)]))
    
    
    
    
