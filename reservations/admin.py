from django.contrib import admin
from custom_admin.admin import admin_site
from .models import Reservation, Consola
# Register your models here.


admin_site.register(Reservation)
admin_site.register(Consola)
