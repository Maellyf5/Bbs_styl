from django import forms

DEMO_CHOICES =( 
    ("Peluquería", "Peluquería"), 
    ("Esteticien", "Esteticien"), 
    ("Otros", "Otros"), 
) 




class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='Correo electronico')
    teléfono = forms.CharField(label='Telefono')



class FormPro(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='Correo Electronico')
    teléfono = forms.CharField(label='Telefono')
    especialidad = forms.ChoiceField(label='Especialidad',choices=DEMO_CHOICES)