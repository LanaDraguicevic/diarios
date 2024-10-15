from django.db import models

class Diarios(models.Model):
    nombre = models.Charfield()
    fecha = models.DateField(null = True, blank = True)
    previsualizacion = models.ImageField(upload_to = , null True, blank = True)
    localidad =

    

