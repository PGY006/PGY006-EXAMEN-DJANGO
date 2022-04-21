from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def productos(request):
    return render(request, 'app/productos.html')

def indexRegistrado(request):
    return render(request,'app/indexRegistrado.html')

def indexSuscrito(request):
    return render(request,'app/indexSuscrito.html')

def inicio(request):
    return render(request,'app/inicio.html')

def planes(request):
    return render(request,'app/planes.html')

def productoRegistrado(request):
    return render(request,'app/productoRegistrado.html')

def productoSuscrito(request):
    return render(request,'app/productoSuscrito.html')

def registro(request):
    return render(request,'app/registro.html')

def seguimiento(request):
    return render(request,'app/seguimiento.html')

def seguimientoSuscrito(request):
    return render(request,'app/seguimientoSuscrito.html')

def carrito(request):
    return render(request,'app/carrito.html')

def carritoDesc(request):
    return render(request,'app/carritoDesc.html')

def carritoNR(request):
    return render(request,'app/carritoNR.html')