from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType



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
    


class CodigoPostal(models.Model):
    codigo = models.IntegerField(null=True)
    
    def __str__(self):         
        return str(self.codigo)



class Servicio(models.Model):
    nombreServicio= models.CharField(max_length=80, null= True)
    imagen = models.ImageField(upload_to='static/img')
    

    def __str__(self):         
        return self.nombreServicio
    

class Especialidades(models.Model):
    nombreEspecialidad= models.CharField(max_length=80, null= True)
    servicio= models.ForeignKey(Servicio, related_name="especialidad",on_delete=models.CASCADE, max_length=80, null= True )

    def __str__(self):         
        return self.nombreEspecialidad

class Precio(models.Model):
    precio = models.IntegerField(null=True)
    nombreEspecialidad = models.ManyToManyField(Especialidades)

      
    def __str__(self):         
        return str(self.precio)


class Profesionales(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    valoracion = models.IntegerField(null=True)
    disponibilidad = models.TextField(max_length=200, null=True,blank=True)
    imagen = models.ImageField(upload_to='static/img')
    nombreEspecialidad = models.ManyToManyField(Especialidades)
    CodigoF = models.ManyToManyField(CodigoPostal)
    precioEspecialidad = models.ManyToManyField(Precio)

   
        
    def __str__(self):         
        return self.nombre
    
class Blog(models.Model):
    EntradaBlog=models.TextField(max_length=200, null=True,blank=True)

    



   


    


