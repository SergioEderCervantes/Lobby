from django.db import models
from users.models import User
# Create your models here.


class Torneo(models.Model):
    MODOS_TORNEO = [
        ("Direct", "Eliminacion directa"),
        ("Double", "Eliminacion doble (loser bracket)"),
        ("Round", "Round Robin"),
    ]
    
    nombre_torneo = models.CharField("Nombre del torneo", max_length=30)
    nombre_juego = models.CharField("Nombre del Juego del que sera el torneo", max_length=30)
    modo_torneo = models.CharField(choices=MODOS_TORNEO, max_length=8, default="Direct")
    imagen = models.ImageField("Imagen del torneo", upload_to='imagen_torneo', null=False, blank=False)


    fecha = models.DateTimeField("Fecha y Hora del torneo")
    is_defined = models.BooleanField(default=False)
    descripcion = models.TextField("Descripcion breve del torneo",max_length=1000, null=True, blank=True)
    reglas = models.TextField("Reglas del torneo (Poner cada regla separada por espacios)", max_length=150,  null=True, blank=True)
    

class Torneo_usuario(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
