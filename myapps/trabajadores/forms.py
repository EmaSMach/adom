from django import forms
from myapps.trabajadores.models import Post, Comentario

class posteoForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ('__all__')
        exclude = ('autor',)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario 
        fields = ('contenido',)
