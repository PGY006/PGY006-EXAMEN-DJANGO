from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key = True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=100, null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_ad = models.DateField(auto_now_add = True)
    updated_ad = models.DateField(auto_now = True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'

class TipoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo_usuario

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
        
class Seguimiento(models.Model):
    codigo = models.IntegerField()
    fecha_pedido = models.DateField()
    hora_pedido = models.IntegerField()
    direccion = models.CharField(max_length=100)
    recibido = models.CharField(max_length=2)


class carritodecompras(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre