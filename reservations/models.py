from django.db import models
from users.models import User
from lobby.models import Sucursal




class Consola(models.Model):
    nombre = models.CharField(max_length=20, blank=False)
    disponibilidad_diaria = models.PositiveIntegerField(default=1, blank=False)
    
    
    def __str__(self):
        return self.nombre
    
    
class Consola_disponibilidad(models.Model):
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField()
    disponibles = models.PositiveBigIntegerField()
    
    class Meta:
        unique_together  = ('consola', 'sucursal', 'fecha')
        
    def __str__(self):
        return f"{self.consola.nombre} en {self.sucursal.nombre_sucursal} el {self.fecha}: {self.disponibles}"
    

class Reservation(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    fecha = models.DateField()
    fecha_reservacion = models.DateField()
    hora = models.TimeField()
    num_personas = models.PositiveIntegerField()
    comentarios = models.TextField(blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    consola_seleccionada = models.ForeignKey(Consola, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reserva de {self.username} para {self.fecha} a las {self.hora}"
