from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# modelo que extiende la tabla user de django, relacion onetoone


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'user= {self.user},name= {self.name}, apellido= {self.lastname} '

# modelo para la tabla contraseñcon relacion a Perfil


class Password(models.Model):
    user_pw = models.ForeignKey(
        Perfil, blank=False, null=False, on_delete=models.CASCADE)
    name_pw = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default='non password')

    def __str__(self) -> str:
        return f'name= {self.name_pw}'
