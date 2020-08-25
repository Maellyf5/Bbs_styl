from django.shortcuts import redirect, render
from django.views.generic import *
from .models import *

# Create your views here.

class Peluquero(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self,**kwargs):
        context=super(Peluquero, self).get_context_data(**kwargs)
        context['mi']= Peluqueros.objects.all()
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:]
        return context
    
class Blog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    context_object_name= 'blog' 
    queryset = EntradaBlog.objects.all()
    

    def get_context_data(self,**kwargs):
        context=super(Blog, self).get_context_data(**kwargs)
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:3]
        #context['template']= 'app:blog' 
        #context['contacto']= Contacto.objects.all()
        #context['mi']= Inicio.objects.all()[0]
        return context 

     
class InfoBlog(DetailView):
    template_name = 'app/infoBlog.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        context = super(InfoBlog, self).get_context_data(**kwargs)
        idblog = self.kwargs.get('pk',None)
        context['info'] = EntradaBlog.objects.get(pk = idblog)
        context['contacto']= Contacto.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:infoblog'
        context['idTemp'] = idblog
        return context     


