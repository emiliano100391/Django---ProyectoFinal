from django.utils import timezone
from django.utils.timezone import now
from django.conf import settings
from django.db import models
from django.contrib import sessions
# Create your models here.
class Publicacion(models.Model):
    autor_public = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo_public = models.CharField(max_length=200,null=False)
    resumen_public = models.TextField()
    contenido_public = models.TextField(blank=True)
    fecha_creacion_public = models.DateTimeField(default=timezone.now)
    fecha_publicacon = models.DateField(blank=True,null=True)
    imagen_public = models.ImageField(upload_to='image/',height_field=None,width_field=None,
                                      help_text='selecciona una imagen para la publicación', 
                                      max_length=100,blank=True,null=True)
    categorias = models.ManyToManyField('Categoria', related_name='Publicacion')

    def publicar(self):
        self.fecha_publicacon=timezone.now()
        self.save()
    def __str__(self):
        return self.titulo_public
    def mostrar_comentarios(self):
        return self.comentarios.filter(aprobado=True)
    def mostrar_imagen(self):
        if self.imagen_public:
            return self.imagen_public.url
       
class Comentario(models.Model):
    publicacion = models.ForeignKey('Publicacion', related_name='comentarios', on_delete=models.CASCADE)
    autor_comentario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body_comentario = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True, editable=False)
    aprobado = models.BooleanField(default=False)

    def aprobar_comentario(self):
        self.aprobado = True
        self.save()

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_categoria
