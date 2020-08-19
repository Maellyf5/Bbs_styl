from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Peluquero.as_view(), name='index'),
    # path('index', Index.as_view(), name='index'),
]