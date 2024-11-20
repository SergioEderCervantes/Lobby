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
    
    fecha = models.DateTimeField("Fecha y Hora del torneo")
    is_defined = models.BooleanField(default=False)
    descripcion = models.TextField("Descripcion breve del torneo",max_length=1000, null=True, blank=True)
    reglas = models.TextField("Reglas del torneo (Poner cada regla separada por espacios)", max_length=150,  null=True, blank=True)
    usuarios_torneo = models.ManyToManyField(User,verbose_name="Usuarios Inscritos al torneo", null= True, blank=True)
    
    class Meta:
        db_table = 'Torneo'
        verbose_name = 'torneo'

    def __str__(self):
        return self.nombre_torneo

