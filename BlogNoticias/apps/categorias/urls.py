from django.urls import path
from . import views

#Este es el nombre del namespace de las url de noticias.
app_name = "categorias"

#Las url son a vistas basadas en clases, por lo que cuando escriba la vista que voy a utilizar tengo que colocar el metodo as view().
urlpatterns = [
    path('listar/', views.Listado_Categorias.as_view(), name = 'path_listado_categorias'),
    ]