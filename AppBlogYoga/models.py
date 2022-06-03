from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 

class Post(models.Model):
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=200)
    cuerpo=models.TextField()
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='blog/', blank=True, null=True)
    categoria=models.CharField(max_length=200, default='yoga')

    def __str__(self):
        return self.titulo+' | '+str(self.autor) 

    def get_absolute_url(self):
        return reverse('home')

class Category(models.Model):
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('home')
    
