from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator



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
    facebook = models.URLField(null=True,blank=True)
    aviso = models.TextField(max_length=10000, null=True,blank=True)
    cookies = models.TextField(max_length=10000, null=True,blank=True)
    
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

class Servicio(models.Model):
    nombreServicio= models.CharField(max_length=80, null= True)
    imagen = models.ImageField(upload_to='static/img')
    

    def __str__(self):         
        return self.nombreServicio

class Precio(models.Model):
    precio = models.IntegerField(null=True)
      
    def __str__(self):         
        return str(self.precio)

class Especialidades(models.Model):
    nombreEspecialidad= models.CharField(max_length=80, null= True)
    servicio= models.ForeignKey(Servicio, related_name="especialidad",on_delete=models.CASCADE, max_length=80, null= True )
    imagen = models.ImageField(upload_to='static/img')
    precio = models.ForeignKey(Precio,on_delete=models.CASCADE, max_length=80, null= True )
    def __str__(self):         
        return self.nombreEspecialidad

class CodigoPostal(models.Model):
    codigo = models.IntegerField(null=True)
    
    def __str__(self):         
        return str(self.codigo)


class Puntuacion(models.Model):
    valoracion = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    def __str__(self):         
        return str(self.valoracion)

class Profesionales(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    disponibilidad = models.TextField(max_length=200, null=True,blank=True)
    imagen = models.ImageField(upload_to='static/img')
    nombreEspecialidades = models.ManyToManyField(Especialidades)
    CodigoPostales = models.ManyToManyField(CodigoPostal,related_name=("profesionales"))
    whatsapp = models.URLField(null= True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null= True,blank=True)
    valoraciones = models.ManyToManyField(Puntuacion)
    PerfilGaleria1 = models.ImageField(upload_to='static/img',blank=True)
    PerfilGaleria2 = models.ImageField(upload_to='static/img',blank=True)
    PerfilGaleria3 = models.ImageField(upload_to='static/img',blank=True)
    PerfilGaleria4 = models.ImageField(upload_to='static/img',blank=True)
    
    def __str__(self):         
        return self.nombre

        
    @property
    def servicios(self):
        serviciosSinRep = []
        for especialidad in self.nombreEspecialidades:
         if especialidad.servicio in serviciosSinRep:
            serviciosSinRep.append(especialidad.servicio)

        return serviciosSinRep


class Conocenos(models.Model):
    conocenos = models.CharField(max_length=50, null=True,blank=True)
    texto = models.TextField(max_length=10000, null=True)
    imagenLogo = models.ImageField(upload_to='static/img')

    def __str__(self):         
        return self.conocenos


    
class Galeria(models.Model):
    imagen = models.ImageField(upload_to='static/img')
    nomImgGaleria = models.CharField(max_length=70)

    def __str__(self):         
        return self.nomImgGaleria


