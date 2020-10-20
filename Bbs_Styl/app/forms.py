from django import forms

DEMO_CHOICES =( 
    ("1", "Tinte"), 
    ("2", "Lavar y peinar"), 
    ("3", "Mechas"), 
) 

class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='correo electronico')
    telefono = forms.CharField(label='telefono')
    peluqueria = forms.ChoiceField(label='peluqueria',choices=DEMO_CHOICES)



class FormPro(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='correo electronico')
    telefono = forms.CharField(label='telefono')
    peluqueria = forms.ChoiceField(label='peluqueria',choices=DEMO_CHOICES)
    

