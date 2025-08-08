from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='categorias')

    def __str__(self):
        return self.nombre

