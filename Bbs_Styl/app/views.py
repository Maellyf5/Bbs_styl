from django.shortcuts import redirect, render
from django.contrib.contenttypes.models import ContentType
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
        context['servi']= Servicio.objects.all()
        context['pelu'] = Profesionales.objects.all()       
        
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
class profesionalCP(DetailView):
    template_name = 'app/profesionalcp.html'
    model = Profesional

    def get_context_data(self,**kwargs):
        context=super(profesionalCP, self).get_context_data(**kwargs)
        idpro = self.kwargs.get('pk',None)
        context['proCP']= Profesional.objects.get(pk = idpro)
        context['servi'] = Servicio.objects.all()
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()

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
        context['pelu'] = Profesionales.objects.all()       
        context['contacto']= Footer.objects.all()

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

        return context


def BuscadorCP(request):
    if request.GET["search"]:
        Buscar= request.GET["search"]
        post= Profesionales.objects.filter(CodigoPostales__codigo=Buscar)
        return render(request,"app/profesionalcp.html", {"post":post, "query":Buscar})



    


""" def buscar(request):
    
    if request.GET["prd"]:
        #mensaje="Articulo buscado: %r" %request.GET["prd"]
        producto= request.GET["prd"]
        articulos = Producto.objects.filter(nombre__icontains=producto) #icontains es como el like de sql asi: like nombre ="raqueta"
        return render(request,"app/resultados_busqueda.html",{"articulos": articulos, "query":producto})
    else:
        mensaje="No has introducido nada"
    
    return HttpResponse(mensaje) """









""" 
class Proyectos(ListView):
    model = Proyecto
    template_name = 'app/proyectos.html'
    context_object_name= 'pro' 
    queryset = Proyecto.objects.all()

 
    def get_context_data(self,**kwargs):
        context=super(Proyectos, self).get_context_data(**kwargs)
        
        context['pro'] = Proyecto.objects.all()
    
        return context 

class Infoproyectos(DetailView):
    template_name = 'app/infoproyectos.html'
    model = Proyecto

    def get_context_data(self,**kwargs):
        context=super(Infoproyectos, self).get_context_data(**kwargs)
        idpro = self.kwargs.get('pk',None)
        context['infop']= Proyecto.objects.get(pk = idpro)
        context['pro'] = Proyecto.objects.all()
        return context """






