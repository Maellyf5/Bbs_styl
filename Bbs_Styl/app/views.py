from django.shortcuts import redirect, render
from django.views.generic import *
from .models import *

# Create your views here.

class Index(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:3]
        context['contacto']= Footer.objects.all()
        return context
    
class Aviso(TemplateView):
    template_name = 'app/avisoLegal.html'

    def get_context_data(self,**kwargs):
        context=super(Aviso, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        return context

class Cookies(TemplateView):
    template_name = 'app/cookies.html'

    def get_context_data(self,**kwargs):
        context=super(Cookies, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        return context

class Blog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    context_object_name= 'blog' 
    queryset = EntradaBlog.objects.all()
    

    def get_context_data(self,**kwargs):
        context=super(Blog, self).get_context_data(**kwargs)
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:3]
        context['mi']= Inicio.objects.all()
        #context['template']= 'app:blog' 
        context['contacto']= Footer.objects.all()
        
        return context 

""" class InfoBlog(DetailView):
    template_name = 'app/infoBlog.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        context = super(InfoBlog, self).get_context_data(**kwargs)
        idblog = self.kwargs.get('pk',None)
        context['info'] = EntradaBlog.objects.get(pk = idblog)
        context['contacto']= Footer.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:infoblog'
        context['idTemp'] = idblog
        return context  """    


