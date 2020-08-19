from django.db import models

# Create your models here.
class Peluqueros(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    textoPerfil = models.TextField(null=True)

    def __str__(self):         
        return self.nombre
