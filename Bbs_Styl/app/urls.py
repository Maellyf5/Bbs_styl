from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inicio/', Index.as_view(), name='inicio'),

    #path('index', Index.as_view(), name='index'),
    path('blog/', Blog.as_view(), name='blog'),
    
]