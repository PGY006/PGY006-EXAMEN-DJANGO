from re import search
from django.contrib import admin
from .models import *
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen','fecha_ingreso']
    search_fields = ['codigo']
    list_per_page = 3

admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','email','password','tipo_usuario']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(TipoUsuario)
admin.site.register(Usuario, UsuarioAdmin)

class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['codigo','fecha_pedido','hora_pedido','direccion','recibido']
    search_fields = ['codigo']
    list_per_page = 3

admin.site.register(Seguimiento, SeguimientoAdmin)

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['nombre','cantidad','precio']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(carritodecompras)