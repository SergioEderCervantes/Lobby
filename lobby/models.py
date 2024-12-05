from django.db import models
from restaurante.models import Producto
from users.models import User

# Create your models here.

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)

    
class Promocion(models.Model):
    descripcion = models.CharField(max_length=100)

    
class Sucursal_Promocion(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)


class Sucursal_Producto(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Comment(models.Model):
    comentario = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  

