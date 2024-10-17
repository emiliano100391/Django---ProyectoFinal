from django.conf import settings
from django.urls import path
from .views import lista_publicaciones, nueva_categoria,nueva_publicacion,publicacion_detalle,publicacion_editar,publicacion_eliminar
from apps.publicaciones import views
from django.conf.urls.static import static

app_name = 'publicaciones'
urlpatterns = [
    path('home/', lista_publicaciones, name='home'),
    path('publicacion_detalle/<int:id>/', publicacion_detalle, name='publicacion_detalle'),
    path('nueva_publicacion/', nueva_publicacion, name='nueva_publicacion'),
    path('publicacion_editar/<int:id>/', publicacion_editar, name='publicacion_editar'),
    path('publicacion_eliminar/<int:id>/', publicacion_eliminar, name='publicacion_eliminar'),
    path('nueva_categoria/',nueva_categoria, name='nueva_categoria'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)