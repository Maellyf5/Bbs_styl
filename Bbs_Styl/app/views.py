from django.shortcuts import redirect, render
from django.contrib.contenttypes.models import ContentType
from django.views.generic import *
from .models import *
from django.http import HttpResponseRedirect
from .forms import Formulario, FormPro
from django.forms import MultipleChoiceField
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from random import choices


# Create your views here.

class Index(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        context['pelu'] = Profesionales.objects.all()       
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:3]
 
        return context

class Blog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    context_object_name= 'blog' 
    paginate_by = 3
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

class InfoBlog(DetailView):
    template_name = 'app/infoBlog.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        context = super(InfoBlog, self).get_context_data(**kwargs)
        idblog = self.kwargs.get('pk',None)
        context['info'] = EntradaBlog.objects.get(pk = idblog)
        context['mi']= Inicio.objects.all()
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


class Conoce(ListView):
    template_name = 'app/conocenos.html'
    context_object_name= 'conoce' 
    queryset = Conocenos.objects.all() 

    def get_context_data(self,**kwargs):
        context=super(Conoce, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        context['pelu'] = Profesionales.objects.all()       
 
        return context


class Colaborador(ListView):
    model = Colaboradores
    template_name = 'app/conocenos.html'
    context_object_name= 'colaborador' 
    queryset = Colaboradores.objects.all() 
   
    def get_context_data(self, **kwargs):
        context=super(Colaborador, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        context['pelu'] = Profesionales.objects.all()       
        context['conoce'] = Conocenos.objects.all() 
    
        return context
        return context
    
class Fotos(TemplateView):
    template_name = 'app/galeria.html'
    model= Galeria
    queryset = Galeria.objects.all() 

    def get_context_data(self,**kwargs):
        context=super(Fotos, self).get_context_data(**kwargs)
        context['mi']= Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        context['fotos'] = Galeria.objects.all() 
        return context  




class Contacto(TemplateView):
    template_name = 'app/contacto.html'
  

    def get_context_data(self,**kwargs):
        context=super(Contacto, self).get_context_data(**kwargs)
        context['contact_form'] =Formulario()
        context['pro'] = Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        return context

    def post(self, request,*args,**kwargs):
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        peluqueria = request.POST.get('peluqueria')

        body= render_to_string(
            'app/email_content.html', {
                'nombre':nombre,
                'mensaje':mensaje,
                'email':email,
                'telefono':telefono,
                'peluqueria':peluqueria
            },
        )

        print(nombre)

        email_message = EmailMessage(
            subject='mensaje de usuario',
            body=body,
            from_email=email,
            to=['koko-yoana@hotmail.es'],
        )
        email_message.content_subtype='html'
        email_message.send()
        return redirect('app:inicio')


class ReProfesional(TemplateView):
    template_name = 'app/reprofesional.html'
  

    def get_context_data(self,**kwargs):
        context=super(ReProfesional, self).get_context_data(**kwargs)
        context['contact_form'] =FormPro()
        context['pro'] = Inicio.objects.all()
        context['contacto']= Footer.objects.all()
        context['servi']= Servicio.objects.all()
        return context

    def post(self, request,*args,**kwargs):
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        especialidad = request.POST.get('especialidad')
        


        body= render_to_string(
            'app/email_content_pro.html', {
                'nombre':nombre,
                'mensaje':mensaje,
                'email':email,
                'telefono':telefono,
                'especialidad':especialidad,



                
            },
        )

        print(nombre)

        email_message = EmailMessage(
            subject='mensaje de usuario',
            body=body,
            from_email=email,
            to=['koko-yoana@hotmail.es'],
        )
        email_message.content_subtype='html'
        email_message.send()
        return redirect('app:inicio')


def main_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'app/profesionales.html', context)
