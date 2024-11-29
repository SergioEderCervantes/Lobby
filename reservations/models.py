from django.db import models
from users.models import User
from lobby.models import Sucursal


<<<<<<< HEAD

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
=======
# Create your models here.

class Reservacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField()
    fecha_reservacion = models.DateField()

>>>>>>> 6481c51628a07f709f72047740b0d016990ac978
