from django.urls import path
from lobby.views import home

urlpatterns = [
        path('', home, name='home'),
]