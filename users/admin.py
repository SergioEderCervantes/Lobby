from django.contrib import admin
from .models import User
from custom_admin.admin import admin_site
# Register your models here.

admin_site.register(User)
