from django.contrib.admin import AdminSite
from django.urls import path
from django.contrib.auth.models import Group, User
from allauth.account.models import EmailAddress
from .views import object_view, save_svg
# Register your models here.


class custom_admin_site(AdminSite):
    site_header = 'Lobby Bar Administration'
    
    def get_urls(self):
        urls =  super().get_urls()
        custom_urls = [
            path('tournaments/tournament_prueba/<int:object_id>/view/', self.admin_view(object_view), name='vista_del_objeto'),
            
        ]
        return custom_urls + urls
    
    

admin_site = custom_admin_site(name='customAdmin')

admin_site.register(User)
admin_site.register(Group)
admin_site.register(EmailAddress)
