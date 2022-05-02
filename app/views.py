from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def productos(request):
    productosAll = Producto.objects.all()
    datos ={
        'listaProductos' : productosAll
    }
    return render(request, 'app/productos.html', datos)

def carrito(request):
    carritosAll = carritodecompras.objects.all()
    datos = {
        'carritoProductos' : carritosAll
    }
    return render(request,'app/carrito.html', datos)

def indexRegistrado(request):
    return render(request,'app/indexRegistrado.html')

def indexSuscrito(request):
    return render(request,'app/indexSuscrito.html')

def inicio(request):
    return render(request,'app/inicio.html')

def planes(request):
    return render(request,'app/planes.html')

def productoRegistrado(request):
    productosAll =Producto.objects.all()
    datos = {
        'listaProductos' : Producto.objects.all()
    }
    return render(request,'app/productoRegistrado.html', datos)

def productoSuscrito(request):
    productosAll =Producto.objects.all()
    datos = {
        'listaProductos' : Producto.objects.all()
    }
    return render(request,'app/productoSuscrito.html', datos)

def registro(request):
    return render(request,'app/registro.html')

def seguimiento(request):
    return render(request,'app/seguimiento.html')

def seguimientoSuscrito(request):
    return render(request,'app/seguimientoSuscrito.html')


def carritoDesc(request):
    carritosAll = carritodecompras.objects.all()
    datos = {
        'carritoProductos' : carritosAll
    }
    return render(request,'app/carritoDesc.html',datos)

def carritoNR(request):
    carritosAll = carritodecompras.objects.all()
    datos = {
        'carritoProductos' : carritosAll
    }
    return render(request,'app/carritoNR.html',datos)

def historialdecompras(request):
    return render(request,'app/historialdecompras.html')


#SeCCION AGREGAR

def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"
    return render(request,'app/agregar_producto.html', datos)

def base(request):
    return render(request,'app/base.html')


