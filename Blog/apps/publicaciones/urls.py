from django.urls import path
from .views import lista_publicaciones,nueva_publicacion,publicacion_detalle,publicacion_editar,publicacion_eliminar
from apps.publicaciones import views

app_name = 'publicaciones'
urlpatterns = [
    path('home/', lista_publicaciones, name='home'),
    path('publicacion_detalle/<int:id>/', publicacion_detalle, name='publicacion_detalle'),
    path('nueva_publicacion/', nueva_publicacion, name='nueva_publicacion'),
    path('publicacion_editar/<int:id>/', publicacion_editar, name='publicacion_editar'),
    path('publicacion_eliminar/<int:id>/', publicacion_eliminar, name='publicacion_eliminar'),
    ]