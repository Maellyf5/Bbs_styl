from django.shortcuts import redirect, render
from django.views.generic import *
from .models import *

# Create your views here.

class Index(TemplateView):
    template_name = 'app/index.html'
