from django import forms
from .models import Noticia

class FormularioCMNoticia(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo','resumen', 'contenido', 'imagen', 'categoria')