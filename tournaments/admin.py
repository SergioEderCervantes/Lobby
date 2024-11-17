from django.contrib import admin
from .models import Torneo
from custom_admin.admin import admin_site
# Register your models here.

class torneoAdmin(admin.ModelAdmin):
    list_display = ('nombre_torneo','nombre_juego','modo_torneo','fecha', 'is_defined')
    readonly_fields = ('is_defined',)


admin_site.register(Torneo,torneoAdmin)