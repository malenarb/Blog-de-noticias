from django.urls import path
from . import views

#Este es el nombre del namespace de las url de noticias.
app_name = "noticias"

#Las url son a vistas basadas en clases, por lo que cuando escriba la vista que voy a utilizar tengo que colocar el metodo as view().
urlpatterns = [
    path('listar', views.Listado_Noticias.as_view(), name = 'path_listado_noticias'),
    path('detalle/<int:pk>', views.Detalle_Noticia.as_view(), name = 'path_detalle_noticias'),
    path('crear/', views.Crear_Noticia.as_view(), name = 'path_creacion_noticias'),
]

