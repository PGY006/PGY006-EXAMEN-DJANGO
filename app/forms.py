from dataclasses import fields
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *

# Creamos un template del formulario


class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=5,max_length=20)
    precio = forms.IntegerField(min_value=400)
    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','tipo','imagen']

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['nombre','precio','imagen']

class UsuarioForm(ModelForm):
    nombre = forms.CharField(min_length=5,max_length=20)
    password = forms.CharField(min_length=5, max_length=50)
    class Meta:
        model = Usuario
        fields = ['codigo','nombre','apellido','email','password','tipo_usuario','imagen']