from django.db import models

# Create your models here.
class Inicio(models.Model):
    imgFondo = models.ImageField(upload_to='static/img')
    textFondo = models.TextField(null=True)
    dscrServicio = models.TextField(null=True)
    imgServi1 = models.ImageField(upload_to='static/img')
    imgServi2 = models.ImageField(upload_to='static/img')
    
    def __str__(self):         
        return self.textFondo

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField(null=True)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='static/img')
    destacados = models.BooleanField(default=False)

    def __str__(self):         
        return self.titulo
    
class Peluqueros(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    textoPerfil = models.TextField(null=True)
    
    def __str__(self):         
        return self.nombre

    