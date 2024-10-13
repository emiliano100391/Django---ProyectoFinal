from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    resume = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usuario=instance)
@receiver(post_save, sender=User)
def guardar_profile(sender, instance, **kwargs):
    instance.profile.save()
