from django.urls import path
from .views import logout_view, profile_view, LoginView, registro

app_name = 'apps.blog_auth'

urlpatterns = [
    path('registro/',registro, name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<username>/', profile_view, name='profile'),
]