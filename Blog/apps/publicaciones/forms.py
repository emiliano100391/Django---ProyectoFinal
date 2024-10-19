from django import forms
from .models import Categoria, Comentario, Publicacion

class NuevaPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo_public', 'resumen_public', 'contenido_public', 'imagen_public','categorias']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        exclude = ('fecha_comentario',)
        #readonly_fields = ['fecha_comentario']
        fields = ['body_comentario']

#--------- FORMS CATEGORIAS ------------#

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']