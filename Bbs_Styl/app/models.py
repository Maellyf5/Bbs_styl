from django.db import models

# Create your models here.
class Peluqueros(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    textoPerfil = models.TextField(null=True)

    def __str__(self):         
        return self.nombre

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField(null=True)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='static/img')
    destacados = models.BooleanField(default=False)

    def __str__(self):         
        return self.titulo