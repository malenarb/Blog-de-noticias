from django.shortcuts import render

#Importo el modelo de noticias para poder trabajar con las instancias de noticas
from .models import Noticia

#Estoy importando las clases genéricas de django para hacer una vista basada en clases
#En este caso voy a tener una vista basada en clases para hacer lo básico 
# (detalle de noticia, listado de noticias, crear, modificar y eliminar noticias)
# y como ya vienen predefinidas por django me ahorra tiempo

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class Listado_Noticias(ListView):
    model = Noticia
    template_name = 'lista_noticias.html'
    context_object_name = 'noticias'
#Coloco que las instancias las voy a llamar por una 
#variable que se llame noticia
    paginate_by= 10
#Esto me permite poder mostrar las noticias de a 10 por página
#En el html le voy a agregar una funcionalidad para poder moverse 
#entre las páginas y ver el resto de las noticias

class Detalle_Noticia(DetailView):
    template_name= 'detalle_noticias.html'
    model = Noticia
    context_object_name = 'noticia'
