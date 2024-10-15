from django.db import models

class Diarios(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.DateField(null = True, blank = True)
    pre_visualizacion = models.ImageField(null = True, blank = True)
    localidad = models.CharField(max_length=16)
    
    

    

