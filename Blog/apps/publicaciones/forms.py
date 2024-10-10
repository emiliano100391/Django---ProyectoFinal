from django.forms import forms,ModelForm
from .models import Publicacion, Categoria,Comentario

class NuevaPublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo_public','resumen_public', 'contenido_public', 'imagen_public']

