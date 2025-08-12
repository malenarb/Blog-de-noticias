from django import forms
from .models import Noticia

class FormularioCrearNoticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo','resumen', 'contenido', 'imagen', 'categoria')