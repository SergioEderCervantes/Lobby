from django.db import models
from users.models import User
from lobby.models import Sucursal
from django.utils.html import format_html




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
        verbose_name = "Disponibilidad consola"
        
    def __str__(self):
        return f"{self.consola.nombre} en {self.sucursal.nombre_sucursal} el {self.fecha}: {self.disponibles}"
    
    def tabla_disponibilidad_por_fecha(self):
        # Obtener todas las consolas para la misma fecha y sucursal
        consolas_del_dia = Consola_disponibilidad.objects.filter(fecha=self.fecha, sucursal=self.sucursal)
        # Crear la cabecera de la tabla
        style_row = "style='border-right: 1px solid var(--border-color); border-left: 1px solid var(--border-color);'"
        header = f"<tr><th {style_row} >Consola</th>"
        disponibilidad_row = f"<tr><td {style_row}>Disponibilidad</td>"
        for consola in consolas_del_dia:
            header += f"<th {style_row}>{consola.consola.nombre}</th>"
            disponibilidad_row += f"<td {style_row}>{consola.disponibles}</td>"
        header += "</tr>"
        disponibilidad_row += "</tr>"
        # Combinar las filas
        tabla = f"<table style='width: 100%;'>{header}{disponibilidad_row}</table>"
        return format_html(tabla)
    


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

    class Meta:
        verbose_name = "Reservacione"


    def __str__(self):
        return f"Reserva de {self.username} para {self.fecha} a las {self.hora}"
