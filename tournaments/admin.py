from django.contrib import admin
from .models import Torneo
from custom_admin.admin import admin_site
# Register your models here.


class Torneo_admin(admin.ModelAdmin):
    list_display = ('nombre_torneo','nombre_juego','modo_torneo','fecha', 'is_defined')
    readonly_fields = ('is_defined',)
    filter_horizontal = ('usuarios_torneo',)


admin_site.register(Torneo,Torneo_admin)