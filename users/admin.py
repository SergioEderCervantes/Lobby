from django.contrib import admin
from .models import User
from custom_admin.admin import admin_site
# Register your models here.



class user_admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_usuario')
    
admin_site.register(User,user_admin)
