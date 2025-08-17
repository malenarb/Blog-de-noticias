from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm 
from apps.noticias.models import Noticia
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.urls import reverse

@login_required
def crear_comentario(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.noticia = noticia
            comentario.save()
            return redirect('noticias:path_detalle_noticias', pk=noticia.id)
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/crear_comentario.html', {'form': form, 'noticia': noticia})

@login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)

    # permiso: solo autor, staff o superuser
    if not (request.user == comentario.autor or request.user.is_staff or request.user.is_superuser):
        return HttpResponseForbidden("No autorizado")

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario actualizado.")
            # redirigir de forma segura desde la vista
            if comentario.noticia_id:
                return redirect('noticias:path_detalle_noticias', pk=comentario.noticia_id)
            return redirect('noticias:path_listado_noticias')
        else:
            messages.error(request, "Hay errores en el formulario. Corrija e intente nuevamente.")
    else:
        form = ComentarioForm(instance=comentario)

    # Construyo return_url en la vista (evita que la plantilla haga reverse con pk vacío)
    if comentario.noticia_id:
        try:
            return_url = reverse('noticias:path_detalle_noticias', kwargs={'pk': comentario.noticia_id})
        except Exception:
            return_url = reverse('noticias:path_listado_noticias')
    else:
        return_url = reverse('noticias:path_listado_noticias')

    return render(request, 'comentarios/editar_comentario.html', {
        'form': form,
        'comentario': comentario,
        'return_url': return_url,
    })

@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)

    # Solo autor, staff o superusuario pueden eliminar
    if not (request.user == comentario.autor or request.user.is_staff or request.user.is_superuser):
        return HttpResponseForbidden("No autorizado")

    noticia_id = comentario.noticia_id  # guardamos para redirigir después
    comentario.delete()
    messages.success(request, "Comentario eliminado correctamente.")

    if noticia_id:
        return redirect('noticias:path_detalle_noticias', pk=noticia_id)
    return redirect('noticias:path_listado_noticias')