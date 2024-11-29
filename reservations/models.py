from django.db import models
from users.models import User
from lobby.models import Sucursal


# Create your models here.

class Reservacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField()
    fecha_reservacion = models.DateField()



    class Meta:
        db_table = 'reservaciones'

    def __str__(self):
        return self.id_reservacion