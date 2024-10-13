from django import forms
from .models import Publicacion

class NuevaPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo_public', 'resumen_public', 'contenido_public', 'imagen_public']
