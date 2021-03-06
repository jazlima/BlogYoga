from django import forms
from .models import Post, Category, Comment

choices=Category.objects.all().values_list('nombre', 'nombre')
choice_list=[]
for item in choices:
    choice_list.append(item)

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
            'categoria': forms.Select(choices= choice_list, attrs={'class': 'form-control'}), 
            'extracto': forms.Textarea(attrs={'class': 'form-control'}),
            
}

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