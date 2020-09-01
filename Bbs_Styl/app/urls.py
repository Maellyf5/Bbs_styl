from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inicio/', Index.as_view(), name='inicio'),
    path('AvisoLegal', Aviso.as_view(), name='avisoLegal'),
    path('cookies', Cookies.as_view(), name='cookies'),
    path('blog/', Blog.as_view(), name='blog'),
    
]