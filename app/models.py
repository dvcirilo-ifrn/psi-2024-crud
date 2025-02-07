from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return self.username


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100, blank=True)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo

class Exemplar(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)