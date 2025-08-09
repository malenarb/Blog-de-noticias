from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.Listado_Noticias.as_view(), name = 'path_listado_noticias'),
    path('detalle/<int:pk>', views.Detalle_Noticia.as_view(), name = 'path_detalle_noticias'),
]

