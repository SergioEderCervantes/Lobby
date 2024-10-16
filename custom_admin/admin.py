from django.contrib.admin import AdminSite
from django.shortcuts import render
from django.urls import path
from django.contrib.auth.models import Group, User
from allauth.account.models import EmailAddress
# Register your models here.


class custom_admin_site(AdminSite):
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

admin_site.register(User)
admin_site.register(Group)
admin_site.register(EmailAddress)
