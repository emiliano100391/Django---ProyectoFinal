from django.contrib import admin
from .models import Publicacion,Categoria, Comentario
from django.utils.safestring import mark_safe

# Register your models here.
class CategoriasInline(admin.StackedInline):
    model = Publicacion.categorias.through
    extra=5

class PostAdmin(admin.ModelAdmin):
    model=Publicacion
    inlines=(CategoriasInline,)
    exclude=('categorias',)
    raw_id_fields=('categorias',)
    list_display=('titulo_public','autor_public','imagen_public','categoria')
    search_fields = ('titulo_public', 'autor_public', 'fecha_creacion_public')
    list_per_page = 25

    readonly_fields =['noticia_img']

    def categoria(self,obj):
        "\n".join([c.nombre_categoria for c in obj.categorias.all()])

    def noticia_img(self,obj):
        return mark_safe(
    '<a href="{0}"><img src="{0}" width="30%"/></a>'.format(self.imagen.url)
    )

fieldsets=(
("Contenido del post",{
"description":"Ingrese la información de título y contenido de la noticia",
"fields":(("titulo_public","autor_public"),"contenido_public","noticia_img","fecha_creacion_public","fecha_publicacion",)
}
),
)


class ComentariosAdmin(admin.ModelAdmin):
    list_display=('autor_comentario', 'body_comentario','publicacion','fecha_comentario', 'aprobado')
    list_filter=('aprobado','fecha_comentario')
    search_fields = ('autor_comentario', 'body_comentario')
    actions=['aprobar_comentarios']

    def aprobar_comentarios(self, request,queryset):
        queryset.update(aprobado=True)

admin.site.register(Categoria,admin.ModelAdmin)
admin.site.register(Publicacion,PostAdmin)
admin.site.register(Comentario,ComentariosAdmin)