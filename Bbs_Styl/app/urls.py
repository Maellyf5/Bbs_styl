from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inicio/', Index.as_view(), name='inicio'),
    path('blog', Blog.as_view(), name='blog'),
    path('infoblog/<int:pk>/', InfoBlog.as_view(), name='infoblog'),
    path('servicios', Servicios.as_view(), name='servicios'),
    path('infoServicios/<int:pk>', InfoServicio.as_view(), name='infoServi'),
    path('AvisoLegal', Aviso.as_view(), name='avisoLegal'),
    path('cookies', Cookies.as_view(), name='cookies'),
    path('profesionales', Profesional.as_view(), name='profesional'),
    path('buscarCP/', BuscadorCP.as_view(), name='profesionalCP'),
    path('conocenos', Conoce.as_view(), name='conocenos'),
    path('galeria',Fotos.as_view(), name='galeria'),
    path('contacto/', Contacto.as_view(), name='contactos'),
    path('registrate/', ReProfesional.as_view(), name='reprofesional'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('PerfilProfesional/<int:pk>', PerfilProfesional.as_view(), name='PerfilProfesional'),
    




    
]