from custom_admin.admin import admin_site
from .models import Users_prueba, Tournament_prueba, Users_admin
# Register your models here.

admin_site.register(Users_prueba, Users_admin)
admin_site.register(Tournament_prueba)
