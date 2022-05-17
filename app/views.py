from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    productosAll = Producto.objects.all()
    datos ={
        'listaProductos' : productosAll
    }
    return render(request, 'app/index.html', datos)

def productos(request):
    productosAll = Producto.objects.all()
    datos ={
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('txtNombre')
        prod.precio = request.POST.get('txtPrecio')
        prod.imagen = request.POST.get('txtImagen')
        prod.save()
    return render(request, 'app/productos.html', datos)

def productosRegistrados(request):
    productosAll = Producto.objects.all()
    datos ={
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('txtNombre')
        prod.precio = request.POST.get('txtPrecio')
        prod.imagen = request.POST.get('txtImagen')
        prod.save()
    return render(request, 'app/productosRegistrados.html', datos)

def indexRegistrado(request):
    return render(request,'app/indexRegistrado.html')

def indexSuscrito(request):
    return render(request,'app/indexSuscrito.html')

def inicio(request):
    return render(request,'app/inicio.html')

def planes(request):
    return render(request,'app/planes.html')

def productoSuscrito(request):
    productosAll = Producto.objects.all()
    datos ={
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('txtNombre')
        prod.precio = request.POST.get('txtPrecio')
        prod.imagen = request.POST.get('txtImagen')
        prod.save()

    return render(request,'app/productoSuscrito.html', datos)

def registro(request):
    return render(request,'app/registro.html')

def seguimiento(request):
    return render(request,'app/seguimiento.html')

def seguimientoSuscrito(request):
    return render(request,'app/seguimientoSuscrito.html')

def carritoDesc(request):
    carritoAll = Carrito.objects.all()
    datos = {
        'listarCarrito' : carritoAll
    }
    if request.method == "POST":
        prod = Carrito()
        prod.id = request.POST.get('id')
        prod.delete()
    return render(request,'app/carritoDesc.html',datos)

def Carro(request):
    carritoAll = Carrito.objects.all()
    datos = {
        'listarCarrito' : carritoAll
    }
    if request.method == "POST":
        prod = Carrito()
        prod.id = request.POST.get('id')
        prod.delete()
    return render(request,'app/carritoDesc.html',datos)

def historialdecompras(request):
    return render(request,'app/historialdecompras.html')

def historialsuscrito(request):
    return render(request,'app/historialsuscrito.html')

#SeCCION AGREGAR

def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"
    return render(request,'app/productos/agregar_producto.html', datos)

def base(request):
    return render(request,'app/base.html')

def agregar_usuario(request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario creado correctamente!"
    return render(request,'app/usuarios/agregar_usuario.html', datos)

def modificarProducto(request, codigo):
    productos =  Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=productos)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES, instance=productos)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente!"
            datos['form'] = formulario
    return render(request,'app/productos/modificarProducto.html', datos)    

def modificarUsuario(request, codigo):
    usuario =  Usuario.objects.get(codigo=codigo)
    datos = {
        'form' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario modificado correctamente!"
            datos['form'] = formulario
    return render(request,'app/usuarios/modificarUsuario.html', datos) 


def listarProductos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    return render(request,'app/productos/listarProductos.html',datos)

def eliminarUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    usuario.delete()
    return redirect(to="listarUsuarios")

def listarUsuarios(request):
    usuariosAll = Usuario.objects.all()
    datos = {
        'listarUsuarios' : usuariosAll
    }
    return render(request,'app/usuarios/listarUsuarios.html',datos)

def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect(to="listarProductos")


def Carro(request):
    carritoAll = Carrito.objects.all()
    datos = {
        'listarCarrito' : carritoAll
    }
    if request.method == "POST":
        prod = Carrito()
        prod.id = request.POST.get('id')
        prod.delete()
    return render(request,'app/carrito.html', datos)

def delete_product(request):
    if request.method == "GET":
        item = Carrito.objects.all()
        item.delete()
        return render(request, "app/finalizado.html")

def delete_product_suscrito(request):
    if request.method == "GET":
        item = Carrito.objects.all()
        item.delete()
        return render(request, "app/finalizadoSuscrito.html")

def empleado(request):
        return render(request, "app/empleado.html")