from django.urls import path
from lobby.views import home, sql

urlpatterns = [
        path('', home, name='home'),
        path('sql/', sql, name='sql'),
]