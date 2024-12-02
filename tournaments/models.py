from django.db import models
from users.models import User
# Create your models here.


class Torneo(models.Model):
    MODOS_TORNEO = [
        ("Direct", "Eliminacion directa"),
        ("Double", "Eliminacion doble (loser bracket)"),
        ("Round", "Round Robin"),
    ]
    
    nombre_torneo = models.CharField("Nombre del torneo", max_length=30, unique=True)
    nombre_juego = models.CharField("Nombre del Juego del que sera el torneo", max_length=30)
    modo_torneo = models.CharField(choices=MODOS_TORNEO, max_length=8, default="Direct")
    imagen = models.ImageField("Imagen del torneo", upload_to='imagen_torneo', null=False, blank=False)


    fecha = models.DateTimeField("Fecha y Hora del torneo")
    is_defined = models.BooleanField(default=False)
    descripcion = models.TextField("Descripcion breve del torneo",max_length=500, null=True, blank=True)
    reglas = models.TextField("Reglas del torneo (Poner cada regla separada por espacios)", max_length=500,  null=True, blank=True)
    jugadores_inscritos = models.ManyToManyField(User,verbose_name="Usuarios Inscritos al torneo", blank=True)
    
    def reglas_como_lista(self):
        # Devuelve un array de cadenas con todas las reglas del torneo
        return self.reglas.splitlines()
        
    def usuarios_inscritos(self):
        # Devuelve un array de cadenas con los usernames de los usuarios inscritos en este torneo.
        return list(self.jugadores_inscritos.values_list('username', flat=True))

    def cantidad_usuarios_inscritos(self):
        # Devuelve el número de usuarios que están inscritos en el torneo
        return self.jugadores_inscritos.count()

    cantidad_usuarios_inscritos.short_description = 'Jugadores Inscritos'
    class Meta:
        db_table = 'Torneo'
        verbose_name = 'torneo'

    def __str__(self):
        return self.nombre_torneo
    
