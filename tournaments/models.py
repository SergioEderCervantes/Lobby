from django.db import models
from django.contrib import admin
# Create your models here.


class Tournament_prueba(models.Model):
    MODOS_DE_TORNEOS = models.TextChoices("Modo de Torneo", "Single 2v2")
    TEXTO_DESCRIPCION = "El tipo de torneo que sera, ya sea de equipos de n jugadores o de un jugador en solitario"
    tournament_id = models.BigAutoField(primary_key=True)
    tournament_name = models.CharField(max_length=30)
    tournament_mode = models.CharField(max_length=20, choices=MODOS_DE_TORNEOS, default="Un Jugador", help_text=TEXTO_DESCRIPCION)
    date = models.DateTimeField()
    def __str__(self):
        return self.tournament_name
    
    class Meta:
        db_table = 'Tournament_pruebas'
        verbose_name = 'torneo'




class Users_prueba(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    tournament_id = models.ForeignKey(Tournament_prueba, verbose_name="ID del torneo que esta inscrito",on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + self.last_name
    class Meta:
        db_table = 'Users_prueba'
        verbose_name = 'prueba usuario'


class Users_admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
