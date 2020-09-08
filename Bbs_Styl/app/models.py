from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating, AbstractBaseRating

# Create your models here.
class Inicio(models.Model):
    imgFondo = models.ImageField(upload_to='static/img')
    textFondo = models.TextField(null=True)
    textServicio = models.TextField(null=True)
    imgServi1 = models.ImageField(upload_to='static/img')
    imgServi2 = models.ImageField(upload_to='static/img')
    proInicio = models.ImageField(upload_to='static/img')
    textProfesional = models.TextField(null=True)
    
    def __str__(self):         
        return self.textFondo

class Footer(models.Model):
    tel = models.IntegerField(null= True,blank=True)
    horario = models.CharField(max_length=80, null=True)
    mail = models.EmailField(null= True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    facebook= models.URLField(null=True,blank=True)
    aviso= models.TextField(max_length=10000, null=True,blank=True)
    cookies= models.TextField(max_length=10000, null=True,blank=True)
    
    
    def __str__(self):         
        return self.mail
 
    

    

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
    precio = models.IntegerField(null=True)
    valoracion=models.IntegerField(null=True)
    disponibilidad=models.CharField(max_length=80,null=True)
    ratings =  GenericRelation(Rating, related_query_name= 'object_list')
    
    def __str__(self):         
        return self.nombre

class MyRating (AbstractBaseRating):
   Peluqueros = models.TextField()

    

    