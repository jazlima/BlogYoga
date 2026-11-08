from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'cuerpo', 'categoria', 'autor', 'extracto', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}), 
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'rivas', 'type':'hidden'}),
            'extracto': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se consulta acá y no al importar el módulo: así migrate puede correr
        # sobre una base vacía y el desplegable toma categorías nuevas.
        self.fields['categoria'].widget = forms.Select(
            choices=[(c.nombre, c.nombre) for c in Category.objects.all()],
            attrs={'class': 'form-control'},
        )

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'cuerpo', 'extracto')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'extracto': forms.Textarea(attrs={'class': 'form-control'}),
            
            
}

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment 
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
}