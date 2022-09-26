from django import forms

class Administrador(forms.Form):
    cod_administrador = forms.IntegerField(primary_key=True)
    email = forms.CharField(max_length=255, null=False)
    Contraseña = forms.CharField(max_length=255, null=False)