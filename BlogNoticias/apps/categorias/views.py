from django.shortcuts import render

#Importo el modelo de categorias para poder trabajar con las instancias de noticas
from .models import Categoria

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy

class Listado_Categorias(ListView):
    model = Categoria
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'

