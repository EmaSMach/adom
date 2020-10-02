from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Perfil, Provincia, Localidad

# from .models import Usuario


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", )


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("foto", "descripcion", "numero_telefono", "categorias", 'localidad', 'calle', 'numero_calle')


class DomicilioForm(forms.Form):
    LOCALIDAD_CHOICES = [(None, '------------')]
    localidades = [pais.nombre for pais in Localidad.objects.filter(provincia__nombre='Chaco')]
    if localidades:
        locs = [(localidad, localidad.title()) for localidad in localidades]
        for l in locs:
            LOCALIDAD_CHOICES.append(l)
    localidad = forms.ChoiceField(choices=LOCALIDAD_CHOICES, required=False)
    calle = forms.CharField(max_length=80, required=False)
    numero = forms.IntegerField(required=False)
