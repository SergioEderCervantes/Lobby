"""
URL configuration for lobby project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from custom_admin.admin import admin_site
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'lobby.views.custom_404'

urlpatterns = [
    path('', include('lobby.urls')),
    path('admin/', admin_site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('reservations/', include('reservations.urls')),
    path('tournaments/', include('tournaments.urls')),
    path('restaurante/', include('restaurante.urls')),
    path('politicas/', include('politicas.urls')),
    path('cookies_servicios/', include('cookies_servicios.urls')),
    path('custom_perfil/', include('custom_perfil.urls')),
    ]