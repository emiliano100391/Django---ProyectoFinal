from django.urls import path
from views import *

app_name = 'apps.blog_auth'

urlpatterns = [
    path('registro.html',SignUpView,name='registro.html')
]