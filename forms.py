from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre, escriba su numbre", required=True)
    email=forms.CharField(label="E-mail correo electronico", required=True)
    contenido=forms.CharField(label="Contenido del mensaje", widget=forms.Textarea)