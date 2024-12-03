from django.db import models
from users.models import User
from lobby.models import Sucursal



class Reservation(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    fecha_reservacion = models.DateField()
    hora = models.TimeField()
    num_personas = models.PositiveIntegerField()
    comentarios = models.TextField(blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.nombre} para {self.fecha} a las {self.hora}"
