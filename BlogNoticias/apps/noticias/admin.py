from django.contrib import admin

# Register your models here.

#Registro mis modelos acá para luego poder verlos desde la página de admin
from .models import Noticia

admin.site.register(Noticia)