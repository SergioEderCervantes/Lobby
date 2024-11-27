from django.contrib import admin
from .models import Producto
from custom_admin.admin import admin_site
# Register your models here.

class Producto_admin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio','tipo_producto')
    
    
admin_site.register(Producto,Producto_admin)
