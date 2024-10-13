from django.urls import reverse, reverse_lazy
from django.utils import timezone
from typing import Any
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from apps.publicaciones.models import Publicacion,Categoria,Comentario
from apps.publicaciones.forms import NuevaPublicacionForm

def base(request):
    return render(request,'base.html')

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.order_by('fecha_publicacon').reverse()[:5]
    context = {
        'lista_publicaciones': publicaciones,
    }
    return render(request, 'home.html', context)
    
def nueva_publicacion(request):
    form = NuevaPublicacionForm()
    if request.method == 'POST':
        form = NuevaPublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor_public = request.user
            publicacion.fecha_creacion_public = timezone.now()
            publicacion.save()
            return redirect('publicaciones:publicacion_detalle', id = publicacion.id)
    else:
        form = NuevaPublicacionForm()
    return render(request, 'nueva_publicacion.html', {'form':form})

def  publicacion_detalle(request,id):
    try:
        data = Publicacion.objects.get(id=id)
        comentarios = Comentario.objects.filter(aprobado=True)
    except Publicacion.DoesNotExist:
        raise Http404('La publicación seleccionada no existe')
    template = 'publicacion_detalle.html'
    context = {
            'publicacion':data,
            'comentarios':comentarios,
            'title':'publicacion_detalle'
        }
    return render(request,template,context)

def publicacion_editar(request, id):
    publicacion = Publicacion.objects.get(id=id)
    if request.method == 'POST':
        form = NuevaPublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor_public = request.user
            publicacion.save()
            return redirect('publicaciones:publicacion_detalle', id = publicacion.id)
    else:
        form = NuevaPublicacionForm(instance=publicacion)
    return render(request, 'nueva_publicacion.html', {'form':form})


def publicacion_eliminar(request, id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()

    return redirect('publicaciones:home')
