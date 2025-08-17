from django.urls import path
from . import views

urlpatterns = [
    path('crear/<int:noticia_id>/', views.crear_comentario, name='crear_comentario'),
    path('editar/<int:pk>/', views.editar_comentario, name='editar_comentario'),
    path('eliminar/<int:pk>/', views.eliminar_comentario, name='eliminar_comentario'),
]
