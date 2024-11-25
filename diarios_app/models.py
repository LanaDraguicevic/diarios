from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class DiarioDisponibilidad(models.Model):
    fecha = models.DateField()
    codigo = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Diario {self.codigo} - {'Disponible' if self.disponible else 'No disponible'}"

class Diarios(models.Model):
    titulo = models.CharField(max_length=20)
    fecha = models.DateField(null=True, blank=True)
    pre_visualizacion = models.ImageField(upload_to='pre-visualizacion/', null=True, blank=True)
    localidad = models.CharField(max_length=16)
    cod = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)], null=True, blank=True)
    
    #Relación con DiarioDisponibilidad
    disponibilidad = models.OneToOneField(DiarioDisponibilidad, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    diario = models.ForeignKey(Diarios, on_delete=models.CASCADE)
    fecha_visita= models.DateTimeField(auto_now_add=True)

    class Meta:
     unique_together = ('usuario', 'diario')

    def __str__(self):
        return self.nombre
    
class DiarioSolicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    diario = models.ForeignKey(Diarios, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.diario.titulo} - {self.fecha_solicitud.strftime('%Y-%m-%d %H:%M:%S')}"

    
