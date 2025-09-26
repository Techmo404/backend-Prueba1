from django.db import models
from datetime import date

# Create your models here.

# modelo de visita con sus caracteristicas
class Visita(models.Model):
    nombre = models.CharField(max_length=100) 
    rut = models.CharField(max_length=12)
    motivo_visita = models.TextField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    fecha = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.nombre} - {self.rut}"

