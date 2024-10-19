from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)