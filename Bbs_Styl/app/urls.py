from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inicio/', Index.as_view(), name='inicio'),
    path('AvisoLegal', Aviso.as_view(), name='avisoLegal'),
    path('cookies', Cookies.as_view(), name='cookies'),
    path('blog', Blog.as_view(), name='blog'),
    path('infoblog/<int:pk>', InfoBlog.as_view(), name= 'infoblog'),
    path('profesionales', Profesional.as_view(), name='profesional'),
    path('servicios', Servicios.as_view(), name='servicios'),
    path('infoServicios/<int:pk>', InfoServicio.as_view(), name='infoServi'),
    path('buscarCP/', BuscadorCP.as_view(), name='profesionalCP'),
    path('contacto/', Contacto.as_view(), name='contactos'),



    
]