from django.urls import reverse, reverse_lazy
from django.utils import timezone
from typing import Any
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from apps.publicaciones.models import Publicacion,Categoria,Comentario
from apps.publicaciones.forms import NuevaCategoriaForm, NuevaPublicacionForm, ComentarioForm

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
    categorias = Categoria.objects.all()
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
    return render(request, 'nueva_publicacion.html', {'form':form, 'categorias':categorias})

def  publicacion_detalle(request,id):
    try:
        data = Publicacion.objects.get(id=id)
        comentarios = Comentario.objects.filter(aprobado=True)
        categoria = data.categorias.all()
        nombre_categorias=categoria.values_list('nombre_categoria',flat=True)
    except Publicacion.DoesNotExist:
        raise Http404('La publicación seleccionada no existe')
    
    publicacion = Publicacion.objects.get(id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario(
                autor_comentario = form.cleaned_data[request.user],
                body_comentario = form.cleaned_data['body_comentario'],
                publicacion = publicacion
            )
            comentario.save()
            return redirect('publicaciones:publicacion_detalle', id = publicacion.id)
    template = 'publicacion_detalle.html'
    context = {
            'publicacion':data,
            'comentarios':comentarios,
            'categorias':nombre_categorias,
            'title':'publicacion_detalle',
            'imagen_public':data.imagen_public
        }
    return render(request,template,context)

def publicacion_editar(request, id):
    publicacion = Publicacion.objects.get(id=id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = NuevaPublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor_public = request.user
            publicacion.save()
            return redirect('publicaciones:publicacion_editar', id = publicacion.id)
    else:
        form = NuevaPublicacionForm(instance=publicacion)
    return render(request, 'publicacion_editar.html', {'form':form, 'publicacion':publicacion, 'categorias':categorias})


def publicacion_eliminar(request, id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()

    return redirect('publicaciones:home')


#------------------- CATEGORIAS-------------------------------#

def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'lista_categorias': categorias,
    }
    return render(request, context)

def nueva_categoria(request):
    if request.method == 'POST':
        form = NuevaCategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            print("Categoría guardada:", categoria)
            return redirect('publicaciones:home')
        else:
            print("Formulario inválido")
            print(form.errors)
    else:
        form = NuevaCategoriaForm()
    return render(request, 'nueva_categoria.html', {'form':form})
        