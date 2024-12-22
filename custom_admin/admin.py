from django.contrib import admin
from django.urls import path
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from .views import tournament_view, save_svg
from lobby.models import Sucursal, Promocion, Comment
from django.forms import ModelForm, ValidationError
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
    
    
# Instanciacion del customAdmin
admin_site = custom_admin_site(name='customAdmin')

# Clases manejadoras y registros de modelos de aplicacion lobby

class Promocion_Form(ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        tiene_vigencia = cleaned_data.get('tiene_vigencia')
        vigencia = cleaned_data.get('vigencia')
        
        if tiene_vigencia and not vigencia:
            raise ValidationError(
                "Debe especificar una fecha de vencimiento si la promocion tiene vigencia"
            )
        return cleaned_data

class Promocion_Admin(admin.ModelAdmin):
    form = Promocion_Form
    list_display = ('nombre', 'tiene_vigencia', 'vigencia', 'es_vigente')
    list_filter = ('tiene_vigencia', 'vigencia')
    ordering = ('-vigencia',)
    
    
class Sucursal_Admin(admin.ModelAdmin):
    list_display = ('nombre_sucursal', 'direccion')
    
    
class Comment_Admin(admin.ModelAdmin):
    list_display = ('comentario', 'fecha', 'usuario')
    ordering = ("-fecha",)
    
    
    
admin_site.register(Promocion,Promocion_Admin)
admin_site.register(Sucursal,Sucursal_Admin)
admin_site.register(Comment,Comment_Admin)


# Clases manejadoras y registro de modelos AllAuth
class EmailAddress_Admin(admin.ModelAdmin):
    list_display = ('email', 'user', 'verified', 'primary')

class SocialAccount_Admin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'uid')

admin_site.register(EmailAddress, EmailAddress_Admin)
admin_site.register(SocialAccount,SocialAccount_Admin)