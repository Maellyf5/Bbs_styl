from django.shortcuts import redirect, render
from django.views.generic import *
from .models import *

# Create your views here.

class Peluquero(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self,**kwargs):
        context=super(Peluquero, self).get_context_data(**kwargs)
        context['mi']= Peluqueros.objects.all()
        return context
