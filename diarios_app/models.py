from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class Diarios(models.Model):
    titulo = models.CharField(max_length=20)
    fecha = models.DateField(null = True, blank = True)
    pre_visualizacion = models.ImageField(upload_to='pre-visualizacion/', null = True, blank = True)
    localidad = models.CharField(max_length=16)
    cod = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)], null = True, blank = True)

class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    diario = models.ForeignKey(Diarios, on_delete=models.CASCADE)
    fecha_visita= models.DateTimeField(auto_now_add=True)

class Meta:
     unique_together = ('usuario', 'diario')

def __str__(self):
        return self.nombre
    
