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

def about(request):
    return render(request,'about.html')