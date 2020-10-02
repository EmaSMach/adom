from django import forms
from myapps.contratos.models import Contrato


class PuntajeForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ('puntaje', 'contratado', 'contratante')


class PuntosForm(forms.Form):
    Contrato.PUNTAJES.insert(0, (None, '----'))
    puntaje = forms.ChoiceField(choices=Contrato.PUNTAJES, required=False)
