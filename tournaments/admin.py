from custom_admin.admin import admin_site
from .models import users_prueba, tournament_prueba, users_admin
# Register your models here.

admin_site.register(users_prueba, users_admin)
admin_site.register(tournament_prueba)
