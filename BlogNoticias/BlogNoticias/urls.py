from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='path_home'),
    path('noticias/', include('apps.noticias.urls', namespace='noticias')),
    path('categorias/', include('apps.categorias.urls', namespace='categorias')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('comentarios/', include(('apps.comentarios.urls', 'comentarios'), namespace='comentarios')),
    #path('home/', views.Home, name = 'path_home'),

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#revisar esto último, no estoy segura de para qué se usaba