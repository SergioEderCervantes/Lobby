from django.contrib import admin
from .models import Torneo
from custom_admin.admin import admin_site
# Register your models here.


class Torneo_admin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('nombre_torneo','nombre_juego','modo_torneo','fecha', 'is_defined')
    #readonly_fields = ('is_defined',)
    filter_horizontal = ('usuarios_torneo',)
=======
    list_display = ('nombre_torneo','nombre_juego','modo_torneo','fecha', 'is_defined', 'imagen')
    readonly_fields = ('is_defined',)
    

    
>>>>>>> 6481c51628a07f709f72047740b0d016990ac978


admin_site.register(Torneo,Torneo_admin)