from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('index.html',index, name="index"),
    path('productos.html',productos, name="productos"),
    path('indexRegistrado.html',indexRegistrado, name="indexRegistrado"),
    path('indexSuscrito.html',indexSuscrito, name="indexSuscrito"),
    path('inicio.html',inicio, name="inicio"),
    path('planes.html',planes, name="planes"),
    path('productoRegistrado.html',productoRegistrado, name="productoRegistrado"),
    path('productoSuscrito.html',productoSuscrito, name="productoSuscrito"),
    path('registro.html',registro, name="registro"),
    path('seguimiento.html',seguimiento, name="seguimiento"),
    path('seguimientoSuscrito.html',seguimientoSuscrito, name="seguimientoSuscrito"),
    path('carrito.html',carrito, name="carrito"),
    path('carritoDesc.html',carritoDesc, name="carritoDesc"),
    path('carritoNR.html',carritoNR, name="carritoNR"),
    path('base.html',base, name="base"),
    path('historialdecompras.html',historialdecompras, name="historialdecompras"),
]