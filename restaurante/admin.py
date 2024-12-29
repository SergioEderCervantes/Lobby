from django.contrib import admin
from .models import Producto, Seccion_productos
from custom_admin.admin import admin_site
# Register your models here.

class Producto_admin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio','seccion_producto')
    list_filter = ('seccion_producto',)
    search_fields = ('nombre_producto', )

class SeccionP_Admin(admin.ModelAdmin):
    list_display = ('nombre_seccion',)
    
admin_site.register(Producto,Producto_admin)
admin_site.register(Seccion_productos, SeccionP_Admin)