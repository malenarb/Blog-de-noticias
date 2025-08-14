from django.db import models
from django.conf import settings
from apps.categorias.models import Categoria  
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=300, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    #autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#habilitado
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    #publicado = models.BooleanField(default=False)#habiltado
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
