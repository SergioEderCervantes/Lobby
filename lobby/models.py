from django.db import models

# Create your models here.

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)

    class Meta:
        db_table = 'sucursal'

    def __str__(self):
        return self.nombre_sucursal
    
class Promocion(models.Model):
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = 'promociones'

    def __str__(self):
        return self.descripcion
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.nombre
    
class SucursalPromocion(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sucursal_promocion'

    def __str__(self):
        return self.id_sucursal_promocion

class SucursalProducto(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sucursal_producto'

    def __str__(self):
        return self.sucursal_producto    

