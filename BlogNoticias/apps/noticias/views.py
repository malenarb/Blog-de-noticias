from django.shortcuts import render

#Importo el modelo de noticias para poder trabajar con las instancias de noticas
from .models import Noticia
from apps.categorias.models import Categoria
#Estoy importando las clases genéricas de django para hacer una vista basada en clases
#En este caso voy a tener una vista basada en clases para hacer lo básico 
# (detalle de noticia, listado de noticias, crear, modificar y eliminar noticias)
# y como ya vienen predefinidas por django me ahorra tiempo

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy
from .forms import FormularioCMNoticia


class Listado_Noticias(ListView):
    model = Noticia
    template_name = 'noticias/lista_noticias.html'
    context_object_name = 'noticias'
#Coloco que las instancias las voy a llamar por una 
#variable que se llame noticia
    paginate_by= 10
#Esto me permite poder mostrar las noticias de a 10 por página
#En el html le voy a agregar una funcionalidad para poder moverse 
#entre las páginas y ver el resto de las noticias

class Detalle_Noticia(DetailView):
    model = Noticia
    template_name= 'noticias/detalle_noticias.html'
    context_object_name = 'noticia'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all().order_by('-creado_en')
        context['user'] = self.request.user  # 👈 Forzamos el usuario al contexto
        return context

#modiFR
class Crear_Noticia(CreateView):
    model = Noticia
    template_name = 'noticias/crear_noticias.html'
    form_class = FormularioCMNoticia
    success_url = reverse_lazy('noticias:path_listado_noticias') #Una vez que la noticia se creo correctamente, a donde voy a redirigir al usuario

class Modificar_Noticia(UpdateView):
    model = Noticia
    template_name = 'noticias/modificar_noticias.html'
    form_class = FormularioCMNoticia
    success_url = reverse_lazy('noticias:path_listado_noticias')

class Eliminar_Noticia(DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:path_listado_noticias')

def Filtrado_Por_Categorias(request, pk):
    categoria_filtro= Categoria.objects.get(pk = pk) 
    noticias_filtradas = Noticia.objects.filter(categoria = categoria_filtro )
    return render (request, 'noticias/filtrado_noticias.html', {'noticias': noticias_filtradas, 'categoria': categoria_filtro})

