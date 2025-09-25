from django.db import models

# Create your models here.
from django.db import models

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=False) 
    fecha = models.DateField(auto_now_add=True)
    motivo_visita = models.TextField()
    hora_entrada = models.TimeField(auto_now_add=True)  
    hora_salida = models.TimeField() 

    def __str__(self):
        return self.nombre