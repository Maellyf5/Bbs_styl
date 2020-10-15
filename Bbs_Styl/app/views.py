from django.shortcuts import redirect, render
from django.contrib.contenttypes.models import ContentType
from django.views.generic import *
from .models import *
from django.http import HttpResponseRedirect


# Create your views here.

class Index(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        context['pelu'] = Profesionales.objects.all()       

 
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
        context['servi']= Servicio.objects.all()
        context['pelu'] = Profesionales.objects.all()       


        return context

class Servicios(ListView):
    template_name = 'app/servicios.html'
    context_object_name= 'servi' 
    queryset = Servicio.objects.all() 
    model = Servicio
    
    def get_context_data(self,**kwargs):
        context=super(Servicios, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['servi']= Servicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['pelu'] = Profesionales.objects.all()       

        return context

class InfoServicio(DetailView):
    template_name = 'app/infoServicio.html'
    model = Servicio

    def get_context_data(self,**kwargs):
        context=super(InfoServicio, self).get_context_data(**kwargs)
        idSer = self.kwargs.get('pk',None)
        context['infoSer']= Servicio.objects.get(pk = idSer)
        context['servi'] = Servicio.objects.all()
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['pelu'] = Profesionales.objects.all()       

        

        return context

class Profesional(ListView):
    template_name = 'app/profesionales.html'
    context_object_name= 'peluqueros' 
    queryset = Profesionales.objects.all() 
    
    def get_context_data(self,**kwargs):
        context=super(Profesional, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        #context['template']= 'app:blog' 
        context['contacto']= Footer.objects.all()
        context['servicios']= Servicio.objects.all()
        context['servi']= Servicio.objects.all()

        return context

class BuscadorCP(TemplateView):
    template_name = 'app/profesionalcp.html'

    def get(self, request, *args, **kwargs):
        Buscar = request.GET.get('search', '')
        self.results = Profesionales.objects.filter(CodigoPostales__codigo=Buscar)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super(BuscadorCP, self).get_context_data(post=self.results, **kwargs)
        context['mi']= Inicio.objects.all()
        context['servi'] = Servicio.objects.all()
        context['contacto']= Footer.objects.all()

        return context

class Aviso(TemplateView):
    template_name = 'app/avisoLegal.html'

    def get_context_data(self,**kwargs):
        context=super(Aviso, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        return context

class Cookies(TemplateView):
    template_name = 'app/cookies.html'

    def get_context_data(self,**kwargs):
        context=super(Cookies, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        return context   