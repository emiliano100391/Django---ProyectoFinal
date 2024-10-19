from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import views, get_user_model,logout
from django.contrib.auth.mixins import LoginRequiredMixin

""" def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            print(user)
            return redirect(reverse_lazy('apps.blog_auth:login'))

        else:
            print(form.errors)
            return render(request, 'auth/registro.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'auth/registro.html', {'form': form}) """
class LoginView(views.LoginView):
    template_name = 'auth/login.html'
    def get_success_url(self):
        return reverse_lazy('publicaciones:lista_publicaciones')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/publicaciones/home/')

class Registro(CreateView):
    template_name = 'auth/registro.html'
    form_class = SignUpForm
    success_url = reverse_lazy('blog_auth:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
    
