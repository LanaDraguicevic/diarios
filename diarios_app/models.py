from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class DiarioDisponibilidad(models.Model):
    fecha = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=100, unique=True)
    disponible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Asegurar que el diario asociado refleje el estado actualizado
        if hasattr(self, 'diario'):
            self.diario.disponibilidad = self
            self.diario.save()

    def __str__(self):
        return f"Diario {self.codigo} - {'Disponible' if self.disponible else 'No disponible'}"


class Diarios(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(null=True, blank=True)
    pre_visualizacion = models.ImageField(upload_to='pre-visualizacion/', null=True, blank=True)
    localidad = models.CharField(max_length=50)
    cod = models.PositiveIntegerField(unique=True, null=True, blank=True)
    disponibilidad = models.OneToOneField(
        DiarioDisponibilidad,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='diario'
    )

    def __str__(self):
        return self.titulo



class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    diario = models.ForeignKey(Diarios, on_delete=models.CASCADE)
    fecha_visita = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'diario')

    def __str__(self):
        return f"{self.usuario.username} visitó {self.diario.titulo}"


class DiarioSolicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    diario = models.ForeignKey(Diarios, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.diario.titulo} - {self.fecha_solicitud.strftime('%Y-%m-%d %H:%M:%S')}"


class Reseña(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    diario = models.ForeignKey(Diarios, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.diario.titulo}"


@receiver(post_save, sender=Diarios)
def create_disponibilidad(sender, instance, created, **kwargs):
    if created and not instance.disponibilidad:
        DiarioDisponibilidad.objects.create(codigo=instance.cod, disponible=True)
