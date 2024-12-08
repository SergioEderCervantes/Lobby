from django.contrib import admin
from .models import Torneo
from custom_admin.admin import admin_site
# Register your models here.


class Torneo_admin(admin.ModelAdmin):
    list_display = ('nombre_torneo','nombre_juego','modo_torneo','fecha', 'is_defined', 'cantidad_usuarios_inscritos')
    #readonly_fields = ('is_defined',)
    filter_horizontal = ('jugadores_inscritos',)
    

    


admin_site.register(Torneo,Torneo_admin)