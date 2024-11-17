from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from users.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
# Register your models here.


class custom_admin_site(admin.AdminSite):
    site_header = 'Lobby Bar Administration'
    
    def get_urls(self):
        urls =  super().get_urls()
        custom_urls = [
            path('prueba/', self.admin_view(self.prueba_view))
        ]
        return custom_urls + urls
    
    def prueba_view(self, request):
        return render(request, 'admin/prueba_view.html')
    

admin_site = custom_admin_site(name='customAdmin')

# Clases manejadoras del display de los modelos del allAuth
class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'verified', 'primary')

class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid')
    
    
admin_site.register(User)
admin_site.register(EmailAddress, EmailAddressAdmin)
admin_site.register(SocialAccount,SocialAccountAdmin)
