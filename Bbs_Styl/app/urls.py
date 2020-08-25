from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Peluquero.as_view(), name='index'),
    path('inicio/', Peluquero.as_view(), name='inicio'),

    #path('index', Index.as_view(), name='index'),
    path('blog/', Blog.as_view(), name = 'blog'),
    
]