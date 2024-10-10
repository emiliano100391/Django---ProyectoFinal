from datetime import timezone
from typing import Any
from unittest import loader
from django.forms import ValidationError
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,DeleteView
from apps.publicaciones.models import Comentario, Publicacion
from apps.publicaciones.forms import NuevaPublicacionForm


def base(request):
    return render(request,'base.html')


class ListaPublicaciones(TemplateView):
    template_name='home'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["lista_publicaciones"] = Publicacion.objects.order_by('fecha_publicacon').reverse()[:5]
        return context
    
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

def NuevaPublicacion(request):
    form = NuevaPublicacionForm()
    if request.method == 'POST':
        form = NuevaPublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save()
            publicacion.autor_public = request.user
            publicacion.fecha_creacion_public = timezone.now()
            publicacion.save()
            return redirect(request, 'publicacion_detalle.html', id = publicacion.id)
    else:
        form = NuevaPublicacionForm()
    return render(request, 'nueva_publicacion.html', {'form':form})