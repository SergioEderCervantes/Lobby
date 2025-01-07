from django.contrib import admin
from custom_admin.admin import admin_site
from .models import Reservation, Consola, Consola_disponibilidad
from django.db.models import Sum, F
from django.db import models
# Register your models here.

class Consola_Disponibilidad_Admin(admin.ModelAdmin):
    list_display = ('fecha', 'tabla_disponibilidad')
    ordering = ('fecha',)
    list_filter = ('fecha',)

    def get_queryset(self, request):
        # Subconsulta para agrupar por fecha y sucursal
        qs = Consola_disponibilidad.objects.filter(
            pk__in=Consola_disponibilidad.objects.values('fecha', 'sucursal')
            .annotate(min_pk=models.Min('pk'))
            .values_list('min_pk', flat=True)
        )
        return qs

    def tabla_disponibilidad(self, obj):
        # Construir la tabla llamando al método del modelo
        return obj.tabla_disponibilidad_por_fecha()

    tabla_disponibilidad.short_description = "Disponibilidad por consola"

    def fecha(self, obj):
        return obj.fecha

    def sucursal(self, obj):
        return obj.sucursal
    
    def has_delete_permission(self, request, obj = None):
        return False
    
    def has_add_permission(self, request):
        return False

    
admin_site.register(Consola_disponibilidad,Consola_Disponibilidad_Admin)
admin_site.register(Reservation)
admin_site.register(Consola)
