from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Producto(models.Model):
    TIPOS_PRODUCTOS= [
        ('A', 'Comida'),
        ('B', 'Bebida sin Alcohol'),
        ('C', 'Cervezas'),
        ('D', 'Bebidas con alcohol'),
        ('E', 'Botellas')
    ]
    nombre_producto = models.CharField(_("Nombre del producto"), max_length=30)
    precio = models.IntegerField(_("Precio del producto"))
    descripcion = models.TextField(_("Descripcion del producto"), blank=True, null=True)
    tipo_producto = models.CharField(_("El tipo de producto"), max_length=2,choices=TIPOS_PRODUCTOS, default='A')
    
    