from django.shortcuts import render
from apps.noticias.models import Noticia
from apps.categorias.models import Categoria

def home(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')[:5]
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {
        'noticias': noticias,
        'categorias': categorias
    })
