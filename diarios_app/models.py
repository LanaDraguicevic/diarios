from django.db import models
from django.core.validators import MaxValueValidator

class Diarios(models.Model):
    titulo = models.CharField(max_length=20)
    fecha = models.DateField(null = True, blank = True)
    pre_visualizacion = models.ImageField(null = True, blank = True)
    localidad = models.CharField(max_length=16)
    cod = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)], null = True, blank = True)


def __str__(self):
        return self.nombre
    
