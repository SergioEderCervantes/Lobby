from django.contrib import admin
from django.urls import path
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from .views import tournament_view, save_svg
# Register your models here.


class custom_admin_site(admin.AdminSite):
    site_header = 'Lobby Bar Administration'
    
    def get_urls(self):
        urls =  super().get_urls()
        custom_urls = [
            path('tournaments/torneo/<int:tournament_id>/view/', 
                 self.admin_view(tournament_view), name='vista_del_torneo'),
            path('save_svg/',self.admin_view(save_svg), name="save_svg")
        ]
        return custom_urls + urls
    
    

admin_site = custom_admin_site(name='customAdmin')

# Clases manejadoras del display de los modelos del allAuth
class EmailAddress_Admin(admin.ModelAdmin):
    list_display = ('email', 'user', 'verified', 'primary')

class SocialAccount_Admin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid')

admin_site.register(EmailAddress, EmailAddress_Admin)
admin_site.register(SocialAccount,SocialAccount_Admin)
