from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Seccion_productos(models.Model):
    class Meta:
        verbose_name = "Seccione"
    nombre_seccion = models.CharField("Nombre de la seccion de productos", max_length=20)
    imagen_respaldo_1 = models.ImageField("Imagen de apoyo 1", upload_to="imagen_seccion", null=False, blank=False)
    imagen_respaldo_2 = models.ImageField("Imagen de apoyo 2", upload_to="imagen_seccion", null=False, blank=False)
    
    def __str__(self):
        return f"Seccion de {self.nombre_seccion}"

class Subseccion_Productos(models.Model):
    nombre_subseccion = models.CharField("Nombre de la subseccion", max_length=20)
    seccion_producto = models.ForeignKey(Seccion_productos, verbose_name="Seccion a la que pertenece el subproducto", null=True, on_delete=models.SET_NULL)
    es_visible = models.BooleanField("Dicta si el nombre de la subseccion se muestra en el menu")
    
    
    def __str__(self):
        return self.nombre_subseccion
    
    
class Producto(models.Model):
    nombre_producto = models.CharField(_("Nombre del producto"), max_length=50)
    precio = models.IntegerField(_("Precio del producto"))
    descripcion = models.TextField(_("Descripcion del producto"), blank=True, null=True)
    subseccion= models.ForeignKey(Subseccion_Productos, verbose_name="Subseccion a la que pertenece el producto", null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.nombre_producto
    
    
