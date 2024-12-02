from django.db import models
from users.models import User
from lobby.models import Sucursal



class Reservation(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    num_personas = models.PositiveIntegerField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva de {self.nombre} para {self.fecha} a las {self.hora}"
