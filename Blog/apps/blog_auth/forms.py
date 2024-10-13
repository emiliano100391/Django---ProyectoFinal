from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
        
class SignInForm(UserCreationForm):
    email = forms.EmailField(label="Email",required=True)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput,max_length=70,required=True)
    password2 = forms.CharField(label="Contraseña",widget=forms.PasswordInput,max_length=70,required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
    def clean(self):
        data = super().clean()
        password1 = data['password1']
        password2 = data['password2']
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return data
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido'
        }