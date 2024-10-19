from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import views, get_user_model,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm

def registro(request):
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
        return render(request, 'auth/registro.html', {'form': form})
class LoginView(views.LoginView):
    template_name = 'auth/login.html'
    def get_success_url(self):
        return reverse_lazy('blog_auth:profile', kwargs={'username': self.request.user.username})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/publicaciones/home/')

def profile_view(request, username):
    user = get_user_model().objects.filter(username=username).first()
    if user:
        profile = user.profile
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu perfil se ha actualizado con éxito')
                return redirect('profile', username=username)
        else:
            form = UserUpdateForm(instance=user)
        return render(request, 'auth/profile.html', {'form': form})
    return redirect('../home')