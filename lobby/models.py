from django.db import models
from restaurante.models import Producto
from users.models import User
from django.utils.timezone import now
# Create your models here.

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)
    
    def __str__(self):
        return f"Sucursal: {self.nombre_sucursal}, Direccion: {self.direccion}"

    
class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField("Imagen de la promocion",upload_to="imagen_promocion", null=False, blank=False)
    tiene_vigencia = models.BooleanField("Tiene vigencia?", default=False, null=False, blank=False)
    vigencia = models.DateField("Vecha de vencimiento", null=True, blank=True)
    
    
    def es_vigente(self):
        if not self.tiene_vigencia:
            return True
        if self.vigencia:
            return self.vigencia >= now().date()
        return False
    
    def __str__(self):
        return f"Promocion: {self.nombre}"

    
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
  

