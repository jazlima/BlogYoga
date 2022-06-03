from xml.sax.xmlreader import AttributesImpl
from django import forms
from .models import Post, Category

choices=Category.objects.all().values_list('nombre', 'nombre')
choice_list=[]
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'cuerpo', 'categoria', 'autor')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}), 
            'categoria': forms.Select(choices= choice_list, attrs={'class': 'form-control'}), 
            
}

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            
            
}