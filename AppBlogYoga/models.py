from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=200)
    cuerpo=RichTextField(blank=True, null=True)
    #cuerpo=models.TextField()
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='images/', blank=True, null=True)
    categoria=models.CharField(max_length=200, default='yoga')
    likes=models.ManyToManyField(User, related_name='blog_post')
    extracto=models.CharField(max_length=200)

    def __str__(self):
        return self.titulo+' | '+str(self.autor) 

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

class Category(models.Model):
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    avatar=models.ImageField(upload_to='images/profile/', blank=True, null=True)
    instagram_url=models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
    
