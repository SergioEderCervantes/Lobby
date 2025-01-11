from django.contrib import admin
from .models import Producto, Seccion_productos, Subseccion_Productos
from custom_admin.admin import admin_site
# Register your models here.

class Producto_admin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio','subseccion')
    list_filter = ('subseccion',)
    search_fields = ('nombre_producto', )

class SeccionP_Admin(admin.ModelAdmin):
    list_display = ('nombre_seccion',)

class SubseccionP_Admin(admin.ModelAdmin):
    list_display = ('nombre_subseccion','seccion_producto')
    
admin_site.register(Producto,Producto_admin)
admin_site.register(Seccion_productos, SeccionP_Admin)
admin_site.register(Subseccion_Productos, SubseccionP_Admin)