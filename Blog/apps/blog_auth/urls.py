from django.urls import path
from .views import logout_view, LoginView, Registro

app_name = 'apps.blog_auth'

urlpatterns = [
    path('registro/',Registro.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]