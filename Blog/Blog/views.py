from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.publicaciones.models import Publicacion


def base(request):
    return render(request,'base.html')


class ListaPublicaciones(TemplateView):
    template_name='home'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["lista_publicaciones"] = Publicacion.objects.order_by('fecha_publicacon').reverse()[:5]
        return context