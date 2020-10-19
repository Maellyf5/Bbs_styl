from django import forms


class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='correo electronico')
    telefono = forms.CharField(label='telefono')


DEMO_CHOICES =( 
    ("1", "Tinte"), 
    ("2", "Lavar y peinar"), 
    ("3", "Mechas"), 
) 


class FormPro(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='correo electronico')
    telefono = forms.CharField(label='telefono')
    peluqueria = forms.MultipleChoiceField(label='peluqueria',choices=DEMO_CHOICES)
    